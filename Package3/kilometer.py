from Package1.position import Units


class Kilometer(Units):
    def __init__(self, measure="km", e_radius=6359):
        super().__init__(measure, e_radius)

