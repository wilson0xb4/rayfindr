from osgeo import ogr
import json


def get_shadow_from_data(sunvector, data):
    """
    Return JSON response using get_shadow_from_points function, and unioning
    polygon shapes into one output.

    Inputs:
        Sunvector: Expected tuple of x and y vector multiplier. This data is
        provided by sun_vector.py.
        Data: Expected polygon shapes from building feature data passed in
        as shape data.

    Output:
        Results: JSON output contains feature data unioned together as one
        complete data package.
    """
    result = None
    multi_building = ogr.Geometry(ogr.wkbMultiPolygon)

    for building in data:
        try:
            geo_building = get_shadow_from_points(sunvector, *building)
        except TypeError:
            continue

        multi_building.AddGeometry(geo_building)
        result = multi_building.UnionCascaded()

    try:
        return json.loads(result.ExportToJson())
    except AttributeError:
        return {"error": "something broke?"}


def get_shadow_from_points(sunvector, height, footprint):
    """Return a geoJSON polygon representing a building shadow.

    Inputs:
    footprint: a list of points representing the base of a building.
        Points are represented by two-length lists [long, lat]
        Format example: [[point1_x, point1_y], [point2_x, point2_y]]
    sunvector: tuple representing the direction and length of the sun's shadow
        projection.
    height: int. The height of the building.

    Output:
    geoJSON object
    """

    projection = []
    vx, vy = sunvector
    height_x = (vx / 3280.4) * 0.009
    height_y = (vy / 3280.4) * 0.009

    footprint = footprint[0]
    for point in footprint:
        proj_point = [
            point[0] + height_x * height,
            point[1] + height_y * height
        ]
        projection.append(proj_point)

    shadow_geometry = ogr.Geometry(ogr.wkbMultiPolygon)
    for i, point in enumerate(footprint[:-1]):
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint(*point)
        ring.AddPoint(*projection[i])
        ring.AddPoint(*projection[i + 1])
        ring.AddPoint(*footprint[i + 1])
        ring.AddPoint(*point)

        poly = ogr.Geometry(ogr.wkbPolygon)
        poly.AddGeometry(ring)
        shadow_geometry.AddGeometry(poly)

    unionpoly = shadow_geometry.UnionCascaded()
    return unionpoly
