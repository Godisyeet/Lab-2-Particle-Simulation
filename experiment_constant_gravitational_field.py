from model import *
from view import *

"""Showcase particles when only a constant gravitational field is applied."""
# Particles have different initial velocities in different directions, velocity_x
# moves continually with the same velocity but velocity_y is affected by the gravitational
# pull which is applied continually with every timestep.

p1 = Particle(1, Vec(-7, 7), Vec(6, 5), 4.5)
p2 = Particle(1, Vec(7, 7), Vec(-6, 6), 3)
p3 = Particle(3, Vec(0, 7), Vec(0, 10), 2)
p4 = Particle(1, Vec(3, 7), Vec(5, 0), 1)

o1 = create_oval(canvas, p1)
o2 = create_oval(canvas, p2)
o3 = create_oval(canvas, p3)
o4 = create_oval(canvas, p4)

pList = [(o1, p1), (o2, p2), (o3, p3), (o4, p4)]

simulation_loop(Forces.constant_gravitational_field, 0, pList)

