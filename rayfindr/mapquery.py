from osgeo import ogr
import json


shpfile = "mapdata/seattle.shp"
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shpfile, 0)


def spatial_filter(la_min, la_max, lo_min, lo_max):
    """Return height and goemetry for buildings in set area.

    args:
        la_min: minimun latitude
        la_max: maximum latitude
        lo_min: minimun longitude
        lo_max: maximum longitude

    returns: a list of tuples containing the height and list of points
            for each building.
    """
    layer = dataSource.GetLayer()

    wkt = (
        "POLYGON (({lo_min} {la_min},"
        " {lo_min} {la_max},"
        " {lo_max} {la_max},"
        " {lo_max} {la_min},"
        " {lo_min} {la_min}))"
        .format(la_min=la_min, la_max=la_max, lo_min=lo_min, lo_max=lo_max)
    )
    layer.SetSpatialFilter(ogr.CreateGeometryFromWkt(wkt))

    buildings = []
    for feature in layer:
        geoJSON = feature.ExportToJson()
        parsed = json.loads(geoJSON)
        height = feature.GetField("BP99_APEX")
        points = parsed['geometry']['coordinates']
        buildings.append((height, points))

    return buildings
