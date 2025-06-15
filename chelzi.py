import turtle
import colorsys

# Configurar la ventana
turtle.bgcolor("black")
t = turtle.Turtle()
t.speed(0)  # máxima velocidad
t.width(2)

# Colores usando el sistema HSV
h = 0
n = 36  # cantidad de figuras

for i in range(360):
    c = colorsys.hsv_to_rgb(h, 1, 1)
    h += 1/n
    t.pencolor(c)
    t.forward(i * 3 / n + i)
    t.left(59)
    t.circle(i * 0.1)

turtle.done()
