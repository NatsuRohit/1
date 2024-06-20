import turtle as t
import colorsys as cs
t.setup(800,800)
t.tracer(10)
t.speed(5)
t.width(1)
t.bgcolor("black")
def square(x):
	for i in range(3):
		t.fd(x)
		t.lt(90)
	t.fd(x)
for j in range(50):
	for i in range(50):
		t.color(cs.hsv_to_rgb(i/10,1-j/20,1))
		t.rt(135)
		square(200-j*4)
		t.rt(135)
		t.circle(50,36)
	t.hideturtle()
t.done()