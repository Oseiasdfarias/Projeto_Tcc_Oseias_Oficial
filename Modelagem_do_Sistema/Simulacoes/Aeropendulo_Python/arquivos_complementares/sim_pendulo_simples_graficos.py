import vpython as vp

scene = vp.canvas(width=450, height=650, align="right",
                  background=vp.vector(0.95, 0.95, 0.95))
scene.range = 25
titulo = "Gráficos dos estados do Pêndulo Simples"
grafico = vp.graph(title=titulo, align="left", xtitle='tempo (s)',
                   fast=True, width=800, height=450,
                   center=vp.vector(0, 12, 0), scroll=True,
                   xmin=0, xmax=20, ymin=-1, ymax=1, dot=True,
                   background=vp.vector(0.95, 0.95, 0.95))

curva1 = vp.gcurve(color=vp.color.blue, width=3,
                   markers=False, label="Posição Angular do Pêndulo",
                   dot=True, dot_color=vp.color.blue)

curva2 = vp.gcurve(color=vp.color.red, width=3,
                   markers=False, label="Velocidade Angular do Pêndulo",
                   dot=True, dot_color=vp.color.red)

curva3 = vp.gcurve(color=vp.color.orange, width=3,
                   markers=False, label="Aceleração Angular do Pêndulo",
                   dot=True, dot_color=vp.color.orange)

motor = vp.box(pos=vp.vector(-20, -20, 0),
               size=vp.vector(2, 2, 2), color=vp.color.blue)
# motor_p2 = vp.box(pos=vp.vector(motor.pos.x, motor.pos.y, motor.pos.z),
#                  size=vp.vector(3, 1, 1), color=vp.color.blue)
pivot = vp.vector(0, 0, 0)
base = vp.box(pos=pivot, size=vp.vec(20, 50, 0), color=vp.color.green)
# roof1 = box(pos=pivot1, size=vector(10, 0.5, 10), color=color.green)
rod = vp.cylinder(pos=pivot, axis=motor.pos-pivot,
                  radius=0.3, color=vp.color.red)

vp.wtext(text="Pêndulo Simple")


g = 9.8
t = 0  # time
dt = 0.01  # time interval
l = vp.mag(motor.pos-pivot)  # length of pendulum
cs = (pivot.y-motor.pos.y)/l  # calculation of cos(theta)
theta = vp.acos(cs)  # angle with vertical direction
vel = 0.0  # angular velocity

while True:
    vp.rate(100)  # maximum 100 calculations per second
    acc = -g/l*vp.sin(theta)  # updating of angular acceleration
    theta = theta+vel*dt  # updating of angular position
    vel = vel+acc*dt  # updating of angular velocity
    # calculating position
    pos_motor = vp.vector(l*vp.sin(theta), pivot.y-l*vp.cos(theta), 0)
    axis_motor = vp.vector(vp.cos(theta), vp.sin(theta), 0)
    motor.pos = pos_motor
    motor.axis = axis_motor
    # motor_p2.axis = axis_motor
    rod.axis = motor.pos  # updating other end of rod of pendulum
    t = t + dt  # updating time
    curva1.plot(t, theta)
    curva2.plot(t, vel)
    curva3.plot(t, acc)
