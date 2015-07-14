from osgeo import ogr
import shapefile


shpfile = "mapdata/seattle.shp"
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shpfile, 0)


def spatial_filter(la_min, la_max, lo_min, lo_max):
    layer = dataSource.GetLayer()

    wkt = (
        "POLYGON (({la_min} {lo_min},"
        " {la_max} {lo_max},"
        " {la_min} {lo_max},"
        " {la_max} {lo_min}))"
        .format(la_min=la_min, la_max=la_max, lo_min=lo_min, lo_max=lo_max)
    )
    layer.SetSpatialFilter(ogr.CreateGeometryFromWkt(wkt))

    
