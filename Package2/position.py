
from math import sin, cos, sqrt, atan2, radians, degrees, pi
from Package1.position import Units
from Package1.position import Geometry


class SphericalGeo(Geometry):
    def __init__(self, obj=None, geometry="spherical"):
        super().__init__(obj, geometry)

    def set_units(self, obj):
        self.__units = obj

    def curry_distance(self, lat, long, pos1):
        radius = self.__units.get_radius()
        lat1 = pos1.get_phi()
        long1 = pos1.get_theta()
        long_diff = long1 - long
        lat_diff = lat1 - lat
        a = sin(lat_diff / 2) ** 2 + cos(lat) * cos(lat1) * sin(long_diff / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))

        return radius * c


class Position:
    def __init__(self, latitude, latitude_s, longitude, longitude_s):
        self.__phi = latitude
        self.__theta = longitude
        self.set_latitude(latitude)
        self.set_longitude(longitude)
        self.__geometry = SphericalGeo(Geometry)
        if latitude_s == "S":
            self.__phi *= - 1
        if longitude_s == "W":
            self.__theta *= -1

    def set_latitude(self, latitude):
        self.set_phi(radians(latitude))

    def get_latitude(self):
        return degrees(self.__phi)

    def set_longitude(self, longitude):
        self.set_theta(radians(longitude))

    def get_longitude(self):
        return degrees(self.__theta)

    def set_phi(self, latitude):
        self.__phi = latitude
        if self.__phi > pi/2 or self.__phi < -pi/2:
            print("The radian of latitude must be in the range of [-π/2, π/2]")
            quit()

    def get_phi(self):
        return self.__phi

    def set_theta(self, longitude):
        self.__theta = longitude
        if self.__theta > pi or self.__theta < -pi:
            print("The radian of longitude must be in the range of [-π, π]")
            quit()

    def get_theta(self):
        return self.__theta

    def set_geometry(self, obj):
        self.__geometry = obj

    def get_geometry(self):
        return self.__geometry

    def distance(self, pos1):
        return self.__geometry.curry_distance(self.__phi, self.__theta, pos1)
