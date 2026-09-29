import math

# Task (2/12): Define a class Vec
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
        return Vec(self.x, self.y)

    def norm(self):
        tup = self.get_coords()
        mult = 0
        for i in tup:
            mult += i**2
        mult = math.sqrt(mult)
        return mult

    
# Task (3/12): Additionally define a function dot(u, v)
def dot(u, v):
    x1, y1 = u.get_coords()
    x2, y2 = v.get_coords()

    return (x1*x2) + (y1*y2)


# Task (4/12): Create a class Particle
class Particle:
    def __init__(self, m, x, v, r):
        self.mass = m
        self.position = x
        self.velocity = v
        self.radius = r
# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).
    def inertial_move(self, dt):
        self.position = dt * self.velocity + self.position

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)
    def apply_force(self, dt, f):
        factor = dt * self.mass
        self.velocity = f.__rmul__(factor) + self.velocity
##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)

    def bounding_box(self):
        t = self.position
        Upper = Vec(t.x - self.radius[0], t.y + self.radius[1])
        Lower = Vec(t.x + self.radius[0], t.y - self.radius[1])
        return Upper, Lower

###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################

class Forces:
    def constant_gravitational_field(dt, particles, g=10):
        for particle in particles:
            downVec = Vec(0, -g*particle[1].mass)
            particle[1].apply_force(dt, downVec.get_coords())
