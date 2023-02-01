
from vpython import *
import numpy as np

s = 'Grafico'
grafico = graph(title=s, xtitle='tempo (s)',
                fast=True, width=800, center=vector(0, 12, 0))
curva = gcurve(color=color.blue, width=4, markers=False, label='Curva')

g = 9.8

bob1 = sphere(pos=vector(-20, -20, 0), radius=0.8, color=color.blue)
pivot1 = vector(0, 0, 0)
base = box(pos=pivot1, size=vec(20, 20, 0), color=color.green)
# roof1 = box(pos=pivot1, size=vector(10, 0.5, 10), color=color.green)
rod1 = cylinder(pos=pivot1, axis=bob1.pos-pivot1, radius=0.3, color=color.red)


t = 0  # time
dt = 0.01  # time interval
l = mag(bob.pos-pivot)  # length of pendulum
cs = (pivot.y-bob.pos.y)/l  # calculation of cos(theta)
theta = acos(cs)  # angle with vertical direction
vel = 0.0  # angular velocity

while (t < 100):
    rate(100)  # maximum 100 calculations per second
    acc = -g/l*sin(theta)  # updating of angular acceleration
    theta = theta+vel*dt  # updating of angular position
    vel = vel+acc*dt  # updating of angular velocity
    # calculating position
    bob.pos = vector(l*sin(theta), pivot.y-l*cos(theta), 0)
    rod.axis = bob.pos-rod.pos  # updating other end of rod of pendulum
    t = t + dt  # updating time
