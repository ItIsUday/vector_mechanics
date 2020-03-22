from math import *


def rounded(func):
    def wrapper(*args, **kwargs):
        ans = func(*args, **kwargs)
        return round(ans, 3) if ans < 10 ** 7 else float('inf')

    return wrapper


class Vector:

    def __init__(self, mag, inclination, h_dist=0, v_dist=0):
        self.mag = mag
        self.inclination = radians(inclination)
        self.h_dist = h_dist
        self.v_dist = v_dist

    def __str__(self):
        return f'Vector: <mag = {round(self.mag, 3)}, inclination = {round(degrees(self.inclination), 3)}>'

    def __repr__(self):
        return f'Vector: <mag = {round(self.mag, 3)}, inclination = {round(degrees(self.inclination), 3)}>'

    def __add__(self, other):
        h_mag_sum = self.h_mag() + other.h_mag()
        v_mag_sum = self.v_mag() + other.v_mag()

        res_mag = sqrt(h_mag_sum ** 2 + v_mag_sum ** 2)
        res_inclination = degrees(atan(v_mag_sum / h_mag_sum))
        moment = self.moment() + other.moment()
        res_h_dist, res_v_dist = self.__get_dist(h_mag_sum, moment, v_mag_sum)

        return Vector(res_mag, res_inclination, res_h_dist, res_v_dist)

    def __radd__(self, other):
        if isinstance(other, Vector):
            return self + other
        return self

    def h_mag(self):
        return self.mag * cos(self.inclination)

    def v_mag(self):
        return self.mag * sin(self.inclination)

    @rounded
    def x_intercept(self):
        return -self.moment() / self.v_mag()

    @rounded
    def y_intercept(self):
        return self.moment() / self.h_mag()

    @rounded
    def moment(self):
        return self.h_mag() * self.v_dist - self.v_mag() * self.h_dist

    @staticmethod
    def __get_dist(h_mag_sum, moment, v_mag_sum):
        if round(v_mag_sum, 3):
            return -moment / v_mag_sum, 0
        elif round(h_mag_sum, 3):
            return 0, moment / h_mag_sum
        else:
            return 0, 0