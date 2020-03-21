from math import *

from vector import Vector


def __get_horizontal_sum(vectors):
    horizontal_sum = sum(vector.horizontal_component().mag for vector in vectors)
    return Vector(horizontal_sum, 0)


def __get_vertical_sum(vectors):
    vertical_sum = sum(vector.vertical_component().mag for vector in vectors)
    return Vector(vertical_sum, 90)


def __get_resultant_mag(h_mag, v_mag):
    return sqrt(h_mag ** 2 + v_mag ** 2)


def __get_resultant_inclination(h_mag, v_mag):
    return degrees(atan(v_mag / h_mag))


def get_resultant(vectors):
    h_mag = __get_horizontal_sum(vectors).mag
    v_mag = __get_vertical_sum(vectors).mag
    resultant_mag = __get_resultant_mag(h_mag, v_mag)
    resultant_inclination = __get_resultant_inclination(h_mag, v_mag)
    return Vector(resultant_mag, resultant_inclination)
