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
        h_comp_sum = self.horizontal_component().mag + other.horizontal_component().mag
        v_comp_sum = self.vertical_component().mag + other.vertical_component().mag

        res_mag = sqrt(h_comp_sum ** 2 + v_comp_sum ** 2)
        res_inclination = degrees(atan(v_comp_sum / h_comp_sum))

        return Vector(res_mag, res_inclination)

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other
        return self

    def horizontal_component(self):
        return Vector(self.mag * cos(self.inclination), 0)

    def vertical_component(self):
        return Vector(self.mag * sin(self.inclination), 90)
