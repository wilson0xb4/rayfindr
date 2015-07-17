import json
import os
from osgeo import ogr


HERE = os.path.dirname(os.path.abspath(__file__))
SHPFILE = os.path.join(HERE, 'mapdata/seattle.shp')


def spatial_filter(la_min, la_max, lo_min, lo_max, datafile=SHPFILE):
    """Return height and goemetry for buildings in set area.

    args:
        la_min: minimun latitude
        la_max: maximum latitude
        lo_min: minimun longitude
        lo_max: maximum longitude

    returns: a list of tuples containing the height and list of points
            for each building.
    """
    shapefile = datafile
    driver = ogr.GetDriverByName('ESRI Shapefile')
    dataSource = driver.Open(shapefile, 0)
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
        try:
            geoJSON = feature.ExportToJson()
            parsed = json.loads(geoJSON)
            height = feature.GetField("BP99_APEX")
            points = parsed['geometry']['coordinates']
        except TypeError:
            continue
        if height > 0:
            buildings.append((height, points))

    return buildings
