from pyramid.view import view_config
import json
# from rayfindr.calculations.sun_pos import time_and_location_to_sun_alt_azimuth as td
from rayfindr.calculations.bounding_box import get_bounding_box as bb
from rayfindr.calculations.sun_vector import get_sun_vector as sv
from rayfindr.calculations.shadows import get_shadow_from_data as shadow
import rayfindr.mapquery as mapquery


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'rayfindr'}


@view_config(route_name='json_test', renderer='json')
def test_json(request):
    return {'text': 'Hello World'}


@view_config(route_name='api_request', renderer='json')
def api_request(request):
    api = json.loads(request.body)
    year = api['year']
    month = api['month']
    day = api['day']
    hour = api['hour']
    lat = api['lat']
    lon = api['lon']

    """box will have four properties - lat_min/max and lon_min/max"""
    box = bb(lat, lon, .25)
    la_min = box.lat_min
    la_max = box.lat_max
    lo_min = box.lon_min
    lo_max = box.lon_max
    """This function will need to get handed to the shadow function and
    then handed to the client"""
    shp_data = mapquery.spatial_filter(la_min, la_max, lo_min, lo_max)

    """vector x and y returned from sun vector"""
    vx, vy = sv(year, month, day, hour, lat, lon)

    geojson = shadow((vx, vy), shp_data)
    return geojson
