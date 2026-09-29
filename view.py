from tkinter import *
from model import *
# Task (7/12): Draw on canvas
def to_canvas_coords(canvas, u):
    x, y = u.__rmul__(canvas.winfo_reqheight()/20)
    y *= -1
    x += canvas.winfo_reqwidth()/2
    y += canvas.winfo_reqheight()/2
    return [x, y]
    

root = Tk()
canvas = Canvas(root, bg="white", width=600, height=600)
canvas.pack()

u = Vec(-2, 10)
v = to_canvas_coords(canvas, u)
pSize = 50


o = canvas.create_oval(v[0]-pSize/2, v[1]-pSize/2, v[0]+pSize/2, v[1]+pSize/2, fill="blue")

input()
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

def create_oval(canvas, particle):
    x = particle.radius[0]/2
    y = particle.radius[1]/2
    particle1 = canvas.create_oval(-x, -y, x, y, fill = "blue")
    new_ball = move_oval_to(canvas, particle1, particle.position[0], particle.position[1])
    return new_ball
# Task (11/12): Define a new function create_oval(canvas, particle)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)
