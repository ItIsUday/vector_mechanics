from math import *


class Vector:

    def __init__(self, mag, inclination):
        self.mag = mag
        self.inclination = radians(inclination)

    def __str__(self):
        return f'Vector: <mag = {self.mag}, inclination = {degrees(self.inclination)}>'

    def __repr__(self):
        return f'Vector: <mag = {self.mag}, inclination = {degrees(self.inclination)}>'

    def __add__(self, other):
        angle = abs(self.inclination - other.inclination)
        res_mag = sqrt(self.mag ** 2 + other.mag ** 2 + 2 * self.mag * other.mag * cos(angle))
        res_inclination = degrees(atan(other.mag * sin(angle) / (self.mag + other.mag * cos(angle))) + self.inclination)

        return Vector(res_mag, res_inclination)

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other
        return self

    def h_mag(self):
        return self.mag * cos(self.inclination)

    def v_mag(self):
        return self.mag * sin(self.inclination)
