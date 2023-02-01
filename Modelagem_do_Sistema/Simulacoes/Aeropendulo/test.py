from vpython import *

# scene.canvas(background=color.white)
canvas(width=1330,height=650,background=color.white)
box_1 = box(pos=vector(0, 0, 0), size=vector(10, 5, 3))

def Rx(v, angle):
    new_y = cos(angle)*v.y - sin(angle)*v.z
    new_z = sin(angle)*v.y + cos(angle)*v.z
    return vector(v.x,new_y,new_z)


def Ry(v,angle):
    new_x = cos(angle)*v.x + sin(angle)*v.z
    new_z = -sin(angle)*v.x + cos(angle)*v.z
    return vector(new_x,v.y,new_z)
 

def Rz(v,angle):
    new_x = cos(angle)*v.x - sin(angle)*v.y
    new_y = sin(angle)*v.x + cos(angle)*v.y
    return vector(new_x,new_y,v.z)


rot = 0
while True:
    rate(100)
    rot_a = rot
    rot += 0.01
    box_1.axis = Ry(box_1.axis, rot-rot_a)
    # box_1.axis = Rx(box_1.axis, pi/300)
    # box_1.axis = Rz(box_1.axis, pi/500)
