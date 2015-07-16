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
    # shp_data = mapquery.spatial_filter(la_min, la_max, lo_min, lo_max)
    shp_data = [(134,
                 [[[-122.34743759673907, 47.620002124254356],
                   [-122.34744247525661, 47.62010098866973],
                   [-122.34743808846338, 47.62010108391565],
                   [-122.34727317909605, 47.62010481158299],
                   [-122.34727416669196, 47.620153654516066],
                   [-122.34716482188362, 47.62015614357774],
                   [-122.34716198619344, 47.620097011188506],
                   [-122.34719142995475, 47.62009635325219],
                   [-122.34718694818761, 47.620007814686666],
                   [-122.34743759673907, 47.620002124254356]]]),
                (150,
                 [[[-122.34829309123728, 47.61997440620047],
                   [-122.34829090755252, 47.619863914437566],
                   [-122.3483911475868, 47.619864153464995],
                   [-122.34839140468321, 47.619938957211424],
                   [-122.34834524324106, 47.619974917444885],
                   [-122.34829309123728, 47.61997440620047]]]),
                (144,
                 [[[-122.34706743432317, 47.619982873048116],
                   [-122.34706734318412, 47.61993931600063],
                   [-122.34714676408609, 47.61993937873061],
                   [-122.34714678618079, 47.61992171007847],
                   [-122.34718088419592, 47.61992173871138],
                   [-122.34718125111932, 47.61983329398087],
                   [-122.34744244750244, 47.619833544591394],
                   [-122.34744202267458, 47.61999345339578],
                   [-122.3471808337001, 47.61999316489142],
                   [-122.34718069930608, 47.61998296779013],
                   [-122.34706743432317, 47.619982873048116]]])]

    """vector x and y returned from sun vector"""
    vx, vy = sv(year, month, day, hour, lat, lon)

    geojson = shadow((vx, vy), shp_data[:2])
    return geojson
