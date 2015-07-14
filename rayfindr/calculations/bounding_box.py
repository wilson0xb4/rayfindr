import math


class BoundingBox(object):
    def __init__(self, *args, **kwargs):
        self.lat_min = None
        self.lon_min = None
        self.lat_max = None
        self.lon_max = None


def get_bounding_box(
        latitude_in_degrees,
        longitude_in_degrees,
        half_side_in_miles):
    assert half_side_in_miles > 0
    assert latitude_in_degrees >= -180.0 and latitude_in_degrees <= 180.0
    assert longitude_in_degrees >= -180.0 and longitude_in_degrees <= 180.0

    half_side_in_km = half_side_in_miles * 1.609344
    lat = math.radians(latitude_in_degrees)
    lon = math.radians(longitude_in_degrees)

    earth_rad = 6371
    # Radius of the parallel at given latitude
    parallel_radius = earth_rad * math.cos(lat)

    lat_min = lat - half_side_in_km / earth_rad
    lat_max = lat + half_side_in_km / earth_rad
    lon_min = lon - half_side_in_km / parallel_radius
    lon_max = lon + half_side_in_km / parallel_radius
    rad2deg = math.degrees

    box = BoundingBox()
    box.lat_min = rad2deg(lat_min)
    box.lon_min = rad2deg(lon_min)
    box.lat_max = rad2deg(lat_max)
    box.lon_max = rad2deg(lon_max)

    return (box)
