import shapely
from meshwell.geometry import Geometry


class PrismClass(Geometry):
    """
    Creates a bottom-up GMSH "prism" formed by a polygon associated with (optional) z-dependent grow/shrink operations.

    Attributes:
        polygons: list of shapely (Multi)Polygon
        buffers: dict of {z: buffer} used to shrink/grow base polygons at specified z-values
        model: GMSH model to synchronize
    """

    def __init__(
        self,
        model,
        polygons,
        buffers,
    ):
        self.model = model

        # Parse buffers
        self.buffered_polygons = self._get_buffered_polygons(polygons, buffers)

        # Track gmsh entities for bottom-up volume definition
        self.points = {}
        self.segments = {}

    def get_gmsh_volumes(self):
        """Returns the fused GMSH volumes within model from the polygons and buffers."""
        volumes = [self._add_volume_with_holes(entry) for entry in self.buffered_polygons]
        if len(volumes) <= 1:
            return volumes
        dimtags = self.model.fuse(
            [(3, volumes[0])],
            [(3, tag) for tag in volumes[1:]],
            removeObject=True,
            removeTool=True,
        )[0]
        self.model.synchronize()
        return [tag for dim, tag in dimtags]

    def _get_buffered_polygons(self, polygons, buffers):
        """Break up polygons on each layer into lists of polygons:z tuples according to buffer entries.

        Arguments (implicit):
            polygons: polygons to bufferize
            buffers: {z: buffer} values to apply to the polygons

        Returns:
            buffered_polygons: list of (z, buffered_polygons)
        """
        all_polygons_list = []
        for polygon in polygons.geoms if hasattr(polygons, "geoms") else [polygons]:
            current_buffers = []
            for z, width_buffer in buffers.items():
                current_buffers.append((z, polygon.buffer(width_buffer, join_style=2)))
            all_polygons_list.append(current_buffers)

        return all_polygons_list

    def _add_volume(self, entry, exterior=True, interior_index=0):
        """Create shape from a list of the same buffered polygon and a list of z-values.
        Args:
            polygons: shapely polygons from the GDS
            zs: list of z-values for each polygon
        Returns:
            ID of the added volume
        """
        bottom_polygon_vertices = self.xy_surface_vertices(
            entry, 0, exterior, interior_index
        )
        gmsh_surfaces = [self._add_surface(bottom_polygon_vertices)]

        top_polygon_vertices = self.xy_surface_vertices(
            entry, -1, exterior, interior_index
        )
        gmsh_surfaces.append(self._add_surface(top_polygon_vertices))

        # Draw vertical surfaces
        for pair_index in range(len(entry) - 1):
            if exterior:
                bottom_polygon = entry[pair_index][1].exterior.coords
                top_polygon = entry[pair_index + 1][1].exterior.coords
            else:
                bottom_polygon = entry[pair_index][1].interiors[interior_index].coords
                top_polygon = entry[pair_index + 1][1].interiors[interior_index].coords
            bottom_z = entry[pair_index][0]
            top_z = entry[pair_index + 1][0]
            for facet_pt_ind in range(len(bottom_polygon) - 1):
                facet_pt1 = (
                    bottom_polygon[facet_pt_ind][0],
                    bottom_polygon[facet_pt_ind][1],
                    bottom_z,
                )
                facet_pt2 = (
                    bottom_polygon[facet_pt_ind + 1][0],
                    bottom_polygon[facet_pt_ind + 1][1],
                    bottom_z,
                )
                facet_pt3 = (
                    top_polygon[facet_pt_ind + 1][0],
                    top_polygon[facet_pt_ind + 1][1],
                    top_z,
                )
                facet_pt4 = (
                    top_polygon[facet_pt_ind][0],
                    top_polygon[facet_pt_ind][1],
                    top_z,
                )
                facet_vertices = [facet_pt1, facet_pt2, facet_pt3, facet_pt4, facet_pt1]
                gmsh_surfaces.append(self._add_surface(facet_vertices))

        # Return volume from closed shell
        surface_loop = self.model.add_surface_loop(gmsh_surfaces)
        return self.model.add_volume([surface_loop])

    def xy_surface_vertices(self, entry, arg1, exterior, interior_index):
        """"""
        # Draw xy surface
        polygon = entry[arg1][1]
        polygon_z = entry[arg1][0]
        return (
            [(x, y, polygon_z) for x, y in polygon.exterior.coords]
            if exterior
            else [
                (x, y, polygon_z) for x, y in polygon.interiors[interior_index].coords
            ]
        )

    def _add_volume_with_holes(self, entry):
        """Returns volume, removing intersection with hole volumes."""
        exterior = self._add_volume(entry, exterior=True)
        interiors = [
            self._add_volume(
                entry,
                exterior=False,
                interior_index=interior_index,
            )
            for interior_index in range(len(entry[0][1].interiors))
        ]
        if interiors:
            for interior in interiors:
                exterior = self.model.cut(
                    [(3, exterior)], [(3, interior)], removeObject=True, removeTool=True
                )
                self.model.synchronize()
                exterior = exterior[0][0][1]  # Parse `outDimTags', `outDimTagsMap'
        return exterior


def Prism(
    model,
    polygons,
    buffers=None,
):
    """Functional wrapper around PrismClass."""
    prism = PrismClass(
        polygons=polygons, buffers=buffers, model=model
    ).get_gmsh_volumes()
    model.synchronize()
    return prism


if __name__ == "__main__":
    # polygon1 = shapely.Polygon(
    #     [[0, 0], [2, 0], [2, 2], [0, 2], [0, 0]],
    #     holes=([[0.5, 0.5], [1.5, 0.5], [1.5, 1.5], [0.5, 1.5], [0.5, 0.5]],),
    # )
    # polygon2 = shapely.Polygon([[-1, -1], [-2, -1], [-2, -2], [-1, -2], [-1, -1]])
    # polygon = shapely.MultiPolygon([polygon1, polygon2])


    # Some complicated (multi)polygon from some upstream calculation
    from shapely import Polygon
    from shapely.plotting import plot_polygon
    import matplotlib.pyplot as plt

    polygon_with_holes = shapely.Polygon(
            [[-2, -2], [3, -2], [3, 2], [-2, 2], [-2, -2]],
            holes=([[0.0, 0.0], 
                    [1.0, 1.0], 
                    [2.0, 0.0], 
                    [1.0, -1.0], 
                    [0.0, 0.0],
                    ],),
        )
    polygon_with_holes_boolean = polygon_with_holes - shapely.Point(-2, -2).buffer(2)

    fig = plt.figure()
    ax = fig.add_subplot()
    plot_polygon(polygon_with_holes_boolean, ax=ax, add_points=False)
    plt.show()

    # Convert to a 2D GMSH entity easily with PolySurface
    import gmsh
    from meshwell.polysurface import PolySurface

    gmsh.clear()
    gmsh.initialize()
    occ = gmsh.model.occ
    poly2D = PolySurface(polygons=polygon_with_holes_boolean, model=occ)
    occ.synchronize()
    gmsh.model.mesh.generate(2)
    gmsh.write("mesh2D.msh")

    # Combine with "buffers" to richly extrude in 3D as a Prism
    buffers = {0.0: -0.2, # z-coordinate: buffer (shrink or grow) to apply to original polygon
               0.2: 0.0,
               0.5: 0.2,
               0.8: 0.0,
               1.0: -0.2,
               }
    
    gmsh.clear()
    gmsh.initialize()
    occ = gmsh.model.occ
    poly3D = Prism(polygons=polygon_with_holes_boolean, buffers=buffers, model=occ)
    occ.synchronize()

    gmsh.model.mesh.generate(3)
    gmsh.write("mesh3D.msh")
