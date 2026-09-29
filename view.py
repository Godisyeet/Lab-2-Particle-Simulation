from tkinter import *
from model import *
import time


# Task (7/12): Draw on canvas
def to_canvas_coords(canvas, u):
    t = u.__rmul__(int(canvas.winfo_reqheight()/20))
    x, y = t.get_coords()
    y *= -1
    x += canvas.winfo_reqwidth()/2
    y += canvas.winfo_reqheight()/2
    return [x, y]
    

root = Tk()
canvas = Canvas(root, bg="white", width=600, height=600)
canvas.pack()

# Task (8/12): Define a new function to_canvas_coords(canvas, x)


#######################################
### NB. Task 9 is done in model.py. ###
#######################################

def move_oval_to(canvas, o, u1 ,u2):
    coord1 = to_canvas_coords(canvas,u1)
    coord2 = to_canvas_coords(canvas,u2)
    
    x1 = coord1[0]
    y1 = coord1[1]
    
    x2 = coord2[0]
    y2 = coord2[1]
    
    canvas.coords(o, x1, y1, x2, y2)
# Task (10/12): Define a new function move_oval_to(o, u1, u2)



# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):
    x = particle.radius[0]/2
    y = particle.radius[1]/2
    particle1 = canvas.create_oval(-x, -y, x, y, fill = "blue")
    new_ball = move_oval_to(canvas, particle1, (particle.position[0] - x, particle.position[1] - y), (particle.position[0] + x, particle.position[1] + y))
    return new_ball

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
p1 = Particle(5, [8, 3], [-2, 0], [2, 2])
p2 = Particle(8, [2, 3], [1, 0], [2, 2])

o1 = create_oval(canvas, p1)
o2 = create_oval(canvas, p2)

particles = [(o1, p1), (o2, p2)]

def simulation_loop(f, timestep, particles):
    
    while True:
        f(timestep, particles)
        timestep = time.time() - timestep
        

        for particle in particles:
            print(timestep)
            particle[1].position[0] += timestep*particle[1].velocity[0]
            particle[1].position[1] += timestep*particle[1].velocity[1]

            move_oval_to(canvas, particle[0], particle[1].bounding_box())

        canvas.update()

simulation_loop(Forces.constant_gravitational_field(), 0, particles)
        