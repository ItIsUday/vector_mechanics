import math


class Vector:

    def __init__(self, mag, inclination):
        self.mag = mag
        self.inclination = math.radians(inclination)

    def __str__(self):
        return f'<mag = {self.mag}, inclination = {math.degrees(self.inclination)}>'

    def __repr__(self):
        return f'<mag = {self.mag}, inclination = {math.degrees(self.inclination)}>'

    def horizontal_component(self):
        return Vector(self.mag * math.cos(self.inclination), 0)

    def vertical_component(self):
        return Vector(self.mag * math.sin(self.inclination), 90)
