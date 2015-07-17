from pyramid.view import view_config
from datetime import datetime
import json
import rayfindr.mapquery as mapquery
from rayfindr.calculations.shadows import get_shadow_from_data as shadow
from rayfindr.calculations.sun_vector import(
    get_sun_vector, get_altitude,
    get_azimuth
)


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
    minute = api['minute']
    lat = api['lat']
    lon = api['lon']
    la_min = api['boundLatMin']
    la_max = api['boundLatMax']
    lo_min = api['boundLonMin']
    lo_max = api['boundLonMax']

    shp_data = mapquery.spatial_filter(la_min, la_max, lo_min, lo_max)

    d_time = datetime(year, month, day, hour, minute)
    altitude = get_altitude(d_time, lat, lon)
    azimuth = get_azimuth(d_time, lat, lon)

    """Check if sun is set"""
    if altitude <= 0:
        return {"error": "night"}

    vx, vy = get_sun_vector(altitude, azimuth)
    geojson = shadow((vx, vy), shp_data)
    return geojson
