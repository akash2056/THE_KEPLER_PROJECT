from .celestial_body import CelestialBody

class Moon(CelestialBody):
    def __init__(self, name, diameter=None, circumference=None):
        super().__init__(name, diameter, circumference)
