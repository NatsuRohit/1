import turtle as t
import colorsys as c
t.setup(800,800)
t.speed(5)
t.tracer(10)
t.width(1)
t.bgcolor("black")
for j in range(100):
    for i in range(100):
        t.color(c.hsv_to_rgb(i/20,j/20,1))
        t.right(90)
        t.circle(200-j*4,90)
        t.left(90)
        t.circle(200-j*4,90)
        t.right(180)
        t.circle(50,24)
t.hideturtle()
t.done()
