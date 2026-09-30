from tkinter import *
from model import *
import time
import random

root = Tk()
canvas = Canvas(root, bg="white", width=800, height=600)
canvas.pack()

def to_canvas_coords(canvas, u):
    u = u.__rmul__(canvas.winfo_reqheight()/20)
    u.y *= -1
    u.x += canvas.winfo_reqwidth()/2
    u.y += canvas.winfo_reqheight()/2
    x, y = u.get_coords()
    return Vec(x, y)

def move_oval_to(canvas, o, u1 ,u2):
    coord1 = to_canvas_coords(canvas,u1)
    coord2 = to_canvas_coords(canvas,u2)
    
    x1 = coord1.x
    y1 = coord1.y
    
    x2 = coord2.x
    y2 = coord2.y

    canvas.coords(o, x1, y1, x2, y2)
    return o

def create_oval(canvas, particle):
    r = particle.radius
    u1 = Vec(particle.position.x - r, particle.position.y - r)
    u2 = Vec(particle.position.x + r, particle.position.y + r)

    colors = [
        "blue", "red", "green", "yellow", "purple", 
        "orange", "pink", "cyan", "magenta", "lime", 
        "gold", "turquoise", "violet", "coral", "deep sky blue"
    ]
    
    particle1 = canvas.create_oval(-r, -r, r, r, fill = random.choice(colors))
    new_ball = move_oval_to(canvas, particle1, u1, u2)
    return new_ball

def simulation_loop(f, timestep, particles):

    lastTime = time.time()
    while True:
        f(timestep, particles)
        now = time.time()
        timestep = now - lastTime
        lastTime = now
        

        for particle in particles:
            particle[1].inertial_move(timestep)
            b1, b2 = particle[1].bounding_box()
            move_oval_to(canvas, particle[0], b1, b2)
            

        canvas.update()