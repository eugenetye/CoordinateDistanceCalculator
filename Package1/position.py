from math import cos, sqrt, radians

class Units:

    def __init__(self, measure="mi", e_radius=3950):
        self.__measure = measure
        self.__e_radius = e_radius

    def set_radius(self, radius):
        self.__e_radius = radius

    def get_radius(self):
        return self.__e_radius

    def set_measure(self, measure):
        self.__measure = measure

    def get_measure(self):
        return self.__measure


class Geometry:

    def __init__(self, obj=None, geometry="planar"):
        self.__units = obj
        self.__geometry = geometry

    def set_units(self, obj):
        self.__units = obj

    def get_units(self):
        return self.__units

    def set_geometry(self, string):
        self.__geometry = string

    def get_geometry(self):
        return self.__geometry

    def curry_distance(self, lat, long, pos1):
        radius = self.__units.get_radius()
        lat1 = pos1.get_latitude()
        long1 = pos1.get_longitude()
        long, lat, long1, lat1 = map(radians, [long, lat, long1, lat1])
        x = (long1 - long) * cos((lat + lat1) / 2)
        y = lat1 - lat
        return radius * sqrt(x**2 + y**2)



class Position:

    def __init__(self, latitude, latitude_s, longitude, longitude_s):
        self.__latitude = latitude
        self.__longitude = longitude
        self.set_latitude(latitude)
        self.set_longitude(longitude)
        self.__geometry = Geometry()
        if latitude_s == "S":
            self.__latitude *= -1
        if longitude_s == "W":
            self.__longitude *= -1

    def set_latitude(self, latitude):
        self.__latitude = latitude
        if self.__latitude > 90 or self.__latitude < -90:
            print("The latitude must be in the range of [-90,90]")
            quit()

    def get_latitude(self):
        return self.__latitude

    def set_longitude(self, longitude):
        self.__longitude = longitude
        if self.__longitude > 180 or self.__longitude < -180:
            print("The longitude must be in the range of [-180,180]")
            quit()

    def get_longitude(self):
        return self.__longitude

    def set_geometry(self, obj):
        self.__geometry = obj

    def get_geometry(self):
        return self.__geometry

    def distance(self, pos1):
        return self.__geometry.curry_distance(self.__latitude, self.__longitude, pos1)
