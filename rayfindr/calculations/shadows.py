from osgeo import ogr


def get_shadow_from_data(sunvector, data):
    geojson_base = {
        "type": "Polygon",
        "coordinates": []
    }
    for building in data:
        geojson = get_shadow_from_points(sunvector, *building)
        geojson_base['coordinates'].push(geojson['coordinates'])
    return geojson_base


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

    # make a list of points representing the projected footprint
    projection = []
    vx, vy = sunvector
    for point in footprint:
        proj_point = [
            point[0] + vx * height,
            point[1] + vy * height
        ]
        projection.append(proj_point)

    # for each footprint edge and matching projection edge, make a shadow poly
    shadowpolys = []
    for i, point in enumerate(footprint[:-2]):
        ring = ogr.Geometry(ogr.wkbLinearRing)
        ring.AddPoint(*point)
        ring.AddPoint(*projection[i])
        ring.AddPoint(*projection[i+1])
        ring.AddPoint(*footprint[i+1])
        ring.AddPoint(*point)

        poly = ogr.Geometry(ogr.wkbPolygon)
        poly.AddGeometry(ring)
        shadowpolys.append(poly)

    # union all the shadow polys together
    unionpoly = shadowpolys[0]
    for poly in shadowpolys[1:]:
        unionpoly = unionpoly.Union(poly)

    # export the resulting shape to geoJSON
    geojson = unionpoly.ExportToJson()
    return geojson

if __name__ == '__main__':
    footprint = [
        [0, 0],
        [1, 0],
        [1, 1],
        [0, 1],
        [0, 0]
    ]
    sunvector = (1, 1)
    height = 2
    print get_shadow_from_points(sunvector, height, footprint)
