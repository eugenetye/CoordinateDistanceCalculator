from Package1 import position
from Package3 import kilometer


class Application(object):

    def __init__(self):
        pass

    @staticmethod
    def assign_coord(pos, unit, geo):
        pos.set_geometry(geo)
        pos.get_geometry().set_units(unit)

    @staticmethod
    def run_example():
        kalamazoo = position.Position(42.2917, "N", 85.5872, "W")
        pos2 = position.Position(51.7434, "S", 34.1121, "W")
        Application.assign_coord(kalamazoo, position.Units(), position.Geometry())
        Application.assign_coord(pos2, position.Units(), position.Geometry())
        print("Distance between position 1 and position 2 is:", kalamazoo.distance(pos2),
              position.Units().get_measure())
