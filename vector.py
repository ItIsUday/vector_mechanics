from math import *


def rounded(func):
    def wrapper(*args, **kwargs):
        return round(func(*args, **kwargs))

    return wrapper


class Vector:

    def __init__(self, mag, inclination, h_dist=0, v_dist=0):
        self.mag = mag
        self.inclination = radians(inclination)
        self.h_dist = h_dist
        self.v_dist = v_dist

    def __str__(self):
        return f'Vector: <mag = {round(self.mag, 3)}, inclination = {round(degrees(self.inclination), 3)}, ' \
               f'h_dist = {round(self.h_dist, 3)}, v_dist = {round(self.v_dist, 3)}>'

    def __repr__(self):
        return f'Vector: <mag = {round(self.mag, 3)}, inclination = {round(degrees(self.inclination), 3)}, ' \
               f'h_dist = {round(self.h_dist, 3)}, v_dist = {round(self.v_dist, 3)}>'

    def __add__(self, other):
        h_mag_sum = self.h_mag() + other.h_mag()
        v_mag_sum = self.v_mag() + other.v_mag()

        res_mag = sqrt(h_mag_sum ** 2 + v_mag_sum ** 2)
        res_inclination = degrees(atan(v_mag_sum / h_mag_sum))

        moment = self.moment() + other.moment()
        res_h_dist = - moment / v_mag_sum

        return Vector(res_mag, res_inclination, res_h_dist, 0)

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other
        return self

    def h_mag(self):
        return self.mag * cos(self.inclination)

    def v_mag(self):
        return self.mag * sin(self.inclination)

    def x_intercept(self):
        return -self.moment() / self.v_mag()

    def y_intercept(self):
        return self.moment() / self.h_mag()

    def moment(self):
        return self.h_mag() * self.v_dist - self.v_mag() * self.h_dist
