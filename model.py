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
        return x,y

    def __add__(self, other):
        x = self.x + other.u
        y = self.y + other.v
        return x, y

    def __sub__(self, other):
        x = self.x - other.u
        y = self.y - other.v
        return x, y

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


# Task (3/12): Additionally define a function dot(u, v)

# Task (4/12): Create a class Particle

# Task (5/12): In the Particle class, implement a method inertial_move(self, dt).

# Task (6/12): In the Particle class, implement a method apply_force(self, dt, f)

##########################################
### NB. Tasks 7–8 are done in view.py. ###
##########################################


# Task (9/12): In the Particle class, add a method bounding_box(self)






###########################################
### When you're done with all 12 tasks: ###
### forces/other features in this file! ###
###########################################