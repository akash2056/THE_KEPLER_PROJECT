from .celestial_body import CelestialBody

class Planet(CelestialBody):
    def __init__(self, name, diameter=None, circumference=None, distanceFromSun=None, orbitalPeriod=None):
        super().__init__(name, diameter, circumference)
        self.distanceFromSun = distanceFromSun
        self.orbitalPeriod = orbitalPeriod
        self.moons = []

    def appendMoon(self, moon):
        self.moons.append(moon)

    def calOrbitalPeriod(self):
        if not self.orbitalPeriod and self.distanceFromSun:
            return (self.distanceFromSun**3)**0.5
        return self.orbitalPeriod

    def calDistanceFromSun(self):
        if not self.distanceFromSun and self.orbitalPeriod:
            return (self.orbitalPeriod**2)**(1 / 3)
        return self.distanceFromSun
