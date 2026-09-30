import math

class Vec:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        coordinate = f"({self.x},{self.y})"
        return coordinate

    def __rmul__(self, factor):
        x = self.x * factor
        y = self.y * factor
        return Vec(x, y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vec(x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        return Vec(x, y)

    def get_coords(self):
        return (self.x, self.y)

    def norm(self):
        tup = self.get_coords()
        mult = 0
        for i in tup:
            mult += i**2
        mult = math.sqrt(mult)
        return mult

def dot(u, v):
    x1, y1 = u.get_coords()
    x2, y2 = v.get_coords()

    return (x1*x2) + (y1*y2)

class Particle:
    def __init__(self, m, x, v, r):
        self.mass = m # float
        self.position = x # vec
        self.velocity = v # vec
        self.radius = r # float

    def inertial_move(self, dt):
        self.position = dt * self.velocity + self.position

    def apply_force(self, dt, f):
        self.velocity = dt * f.__rmul__(1/self.mass) + self.velocity

    def bounding_box(self):
        t = self.position
        Upper = Vec(t.x - self.radius, t.y + self.radius)
        Lower = Vec(t.x + self.radius, t.y - self.radius)
        return Upper, Lower

class Forces:
    def constant_gravitational_field(dt, particles, g=10):
        for particle in particles:
            downVec = Vec(0, -g*particle[1].mass)
            particle[1].apply_force(dt, downVec)
