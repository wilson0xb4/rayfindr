from osgeo import ogr
import json
import shapefile


shpfile = "mapdata/seattle.shp"
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shpfile, 0)

LA_MIN = 47.61678170542361
LA_MAX = 47.62401829457639
LO_MIN = -122.34373192438086
LO_MAX = -122.35446807561914


def spatial_filter(la_min, la_max, lo_min, lo_max):
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

    # Loop through the records and compose
    buildings = []
    for feature in layer:
        geoJSON = feature.ExportToJson()
        parsed = json.loads(geoJSON)
        height = feature.GetField("BP99_APEX")
        points = parsed['geometry']['coordinates']
        buildings.append((height, points))

    return buildings
