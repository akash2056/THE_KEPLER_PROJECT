import math

class CelestialBody:
    def __init__(self, name, diameter=None, circumference=None):
        self.name = name
        self.diameter = diameter
        self.circumference = circumference

    def calCircumference(self):
        if self.diameter:
            return math.pi * self.diameter
        return self.circumference

    def calDiameter(self):
        if self.circumference:
            return self.circumference / math.pi
        return self.diameter

    def calVolume(self):
        if self.diameter:
            radius = self.diameter / 2
            return (4 / 3) * math.pi * radius**3
        return None
