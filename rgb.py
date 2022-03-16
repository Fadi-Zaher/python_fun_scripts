from turtle import *
from colorsys import *
from random import choice

bgcolor("black")
x = 1
hue = 0
tracer(200)
width(2)
ht()
ranges = [1,2,3,4,5,6]

for i in range(3600):
	color(hsv_to_rgb(hue,1,1))
	pd()
	rt(x)
	fd(200)
	rt(30)
	fd(120)
	rt(30)
	fd(60)
	pu()
	home()
	hue += 0.0027
	x+=0.1
done()