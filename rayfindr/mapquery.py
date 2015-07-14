from osgeo import ogr
import shapefile


shapefile = "mapdata/seattle.shp"
driver = ogr.GetDriverByName('ESRI Shapefile')
dataSource = driver.Open(shapefile, 0)


def spatial_filter(la_min, la_max, lo_min, lo_max):
    layer = dataSource.GetLayer()


