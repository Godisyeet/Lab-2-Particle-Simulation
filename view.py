from tkinter import *
from model import *
import time
# Task (7/12): Draw on canvas
def to_canvas_coords(canvas, u):
    u = u.__rmul__(canvas.winfo_reqheight()/20)
    u.y *= -1
    u.x += canvas.winfo_reqwidth()/2
    u.y += canvas.winfo_reqheight()/2
    return u.get_coords()
    

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
    
    x1 = coord1.x
    y1 = coord1.y
    
    x2 = coord2.x
    y2 = coord2.y

    canvas.coords(o, x1, y1, x2, y2)
    return o
# Task (10/12): Define a new function move_oval_to(o, u1, u2)



# Task (11/12): Define a new function create_oval(canvas, particle)
def create_oval(canvas, particle):
    x = particle.radius[0]/2
    y = particle.radius[1]/2
    u1 = Vec(particle.position.x - x, particle.position.y - y)
    u2 = Vec(particle.position.x + x, particle.position.y + y)

    particle1 = canvas.create_oval(-x, -y, x, y, fill = "blue")
    new_ball = move_oval_to(canvas, particle1, u1, u2)
    print(str(new_ball))
    return new_ball

# Task (12/12): Define a function simulation_loop(f, timestep, particles)

p1 = Particle(0.5, Vec(-5, 3), Vec(3, 0), [1, 1])
p2 = Particle(1, Vec(3, 3), Vec(-3, 10), [1, 1])

o1 = create_oval(canvas, p1)
o2 = create_oval(canvas, p2)

particleList = [(o1, p1), (o2, p2)]

canvas.update()



def simulation_loop(f, timestep, particles):

    lastTime = time.time()
    while True:
        f(timestep, particles)
        now = time.time()
        timestep = now - lastTime
        lastTime = now
        

        for particle in particles:
            particle[1].position.x += timestep*particle[1].velocity.x
            particle[1].position.y += timestep*particle[1].velocity.y
            b1, b2 = particle[1].bounding_box()
            move_oval_to(canvas, particle[0], b1, b2)
            

        canvas.update()

simulation_loop(Forces.constant_gravitational_field, 0, particleList)
