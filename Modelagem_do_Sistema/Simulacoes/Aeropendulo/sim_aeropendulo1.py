import vpython as vp


scene = vp.canvas(title='<h1>Pêndulo</h1>', autoscale=0, range=5,
                  center=vp.vec(0, 3, 0), forward=vp.vec(-0.3, 0, -1))

# Ambiente de sinulação.
base = vp.box(pos=vp.vec(0, -0.85, 0), size=vp.vec(20, 0.1, 10),
              texture=vp.textures.wood)
parede = vp.box(pos=vp.vec(0, 7.1, -5.05), size=vp.vec(20, 16, 0.1),
                color=vp.vec(0.7, 0.7, 0.7))
sitio = vp.text(pos=vp.vec(0, 7.1, -5), text="AEROPÊNDULO",
                color=vp.color.black, align='center', depth=0)

# Braço do Aeropêndulo.
barra = vp.box(pos=vp.vec(0, -1.4, 0), size=vp.vec(0.2, 3.2, 0.2),
               color=vp.vec(1, 1, 0))

# Base que acopla o motor ao braço.
base_motor = vp.cylinder(pos=vp.vec(-0.2, -3, 0), radius=0.5,
                         axis=vp.vec(0.4, 0, 0),
                         color=vp.vec(0.5, 0.5, 0.8))
# Armadura do motor.
base2_motor = vp.box(pos=vp.vec(-0.4, -3, 0), size=vp.vec(0.4, 0.4, 0.4),
                     color=vp.vec(1, 1, 0))

# Eixo que da hélice do motor.
base_helice = vp.cylinder(pos=vp.vec(-0.8, -3, 0), radius=0.05,
                          axis=vp.vec(0.4, 0, 0),
                          color=vp.vec(0.5, 0.5, 0.8))

# Hélice.
helice = vp.box(pos=vp.vec(-0.8, -3, 0), size=vp.vec(0.05, 0.2, 2),
                color=vp.vec(1, 1, 0))

# Motor completo.
motor = vp.compound([base_motor, base2_motor, base_helice])

# Motor + Hélice.
motor_helice = vp.compound([motor, helice])

# Aeropêndulo
pendulo = vp.compound([barra, motor_helice])
pendulo.pos = vp.vec(-0.31, 1.8, 0)

# Eixo de sustentação.
eixo = vp.cylinder(pos=vp.vec(0, 3.5, 0.3), radius=0.09,
                   axis=vp.vec(0, 0, -2),
                   color=vp.vec(0.7, 0.4, 0.1))

# Estrutura de sustentação do aeropêndulo.
b1 = vp.box(pos=vp.vec(0, 1.7, -2), size=vp.vec(1, 4.2, 0.6),
            color=vp.vec(0.7, 0.4, 0.1))
b2 = vp.box(pos=vp.vec(0, -0.6, -1.5), size=vp.vec(3, 0.4, 1.6),
            color=vp.vec(0.7, 0.4, 0.1))

pendulo.w = 10
pendulo.angulo = 0
pendulo.l = 3
dt = 0.01

while True:
    vp.rate(50)
    pendulo.a = -98*vp.sin(pendulo.angulo)/pendulo.l
    pendulo.w = pendulo.w + pendulo.a*dt
    pendulo.angulo = pendulo.angulo + pendulo.w*dt
    pendulo.rotate(axis=vp.vec(0, 0, 1), angle=pendulo.w*dt,
                   origin=vp.vec(0, 3.5, 0))
