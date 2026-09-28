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

# Task (10/12): Define a new function move_oval_to(o, u1, u2)

# Task (11/12): Define a new function create_oval(canvas, particle)

# Task (12/12): Define a function simulation_loop(f, timestep, particles)