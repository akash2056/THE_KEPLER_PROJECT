from .celestial_body import CelestialBody

class Sun(CelestialBody):
    def __init__(self, name, diameter=None, circumference=None):
        super().__init__(name, diameter, circumference)
        self.planets = []

    def appendPlanet(self, planet):
        self.planets.append(planet)
