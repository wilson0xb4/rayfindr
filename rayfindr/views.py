from pyramid.view import view_config
from pyramid.response import Response
import json
from rayfindr.calculations.sun_pos import\
    time_and_location_to_sun_alt_azimuth as td
from rayfindr.calculations.bounding_box import get_bounding_box as bb
from rayfindr.calculations.sun_vector import get_sun_vector as sv
from rayfindr.mapquery import spacial_filter as sf


@view_config(route_name='home', renderer='templates/mytemplate.pt')
def my_view(request):
    return {'project': 'rayfindr'}


@view_config(route_name='json_test', renderer='json')
def test_json(request):
    return {'text': 'Hello World'}


@view_config(route_name='api_request', renderer='json')
def api_request(request):
    # api = json.loads(request)
    # year = api['year']
    # month = api['month']
    # day = api['day']
    # hour = api['hour']
    # lat = api['lat']
    # lon = api['lon']

    # """box will have four properties - lat_min/max and lon_min/max"""
    # box = bb(lat, lon, .25)
    # la_min = box.lat_min
    # la_max = box.lat_max
    # lo_min = box.lon_min
    # lo_max = box.lon_max
    # """This function will need to get handed to the shadow function and then handed to the client"""
    # shp_data = sf(la_min, la_max, lo_min, lo_max)
    # """altitude and azimuth returned from sun position"""
    # alt, az = td(year, month, day, hour, lat, lon)
    # """vector x and y returned from sun vector"""
    # vx, vy = sv(az, alt)

    # return Response(
    #     body=json.dumps({
    #         'alt': alt,
    #         'az': az,
    #         'vx': vx,
    #         'vy': vy
    #     }), content_type=b'application/json')

    return Response(
        body=json.dumps({
            [(700, [[-122.34926163617325, 47.62045662658992],
                    [-122.3492899953147, 47.62045422022144],
                    [-122.34931737329691, 47.62045983255712],
                    [-122.34933899282515, 47.62047248728353],
                    [-122.3493511421282, 47.62049001180723],
                    [-122.3493517052271, 47.62050933515622],
                    [-122.34934058549076, 47.62052714175043],
                    [-122.34931971995441, 47.62054036239886],
                    [-122.34929269013196, 47.6205466994618],
                    [-122.34926421357345, 47.620545078034866],
                    [-122.34923916172738, 47.62053573190211],
                    [-122.34922188030394, 47.62052030524769],
                    [-122.34921541042033, 47.62050147169665],
                    [-122.34922077815231, 47.620482480474244],
                    [-122.34923714826462, 47.620466632582506],
                    [-122.34926163617325, 47.62045662658992]])]
        }), content_type=b'application/json')
