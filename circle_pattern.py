# Circle Pattern Code
import turtle
import colorsys
import time

obj = turtle.Turtle()
scr = turtle.Screen()

scr.bgcolor('black')
time.sleep(2)
obj.speed(0)

n = 72
height = 0

for i in range(360):
    col = colorsys.hsv_to_rgb(height, 1, 0.7)
    height = height + 1/n

    obj.color(col)
    obj.circle(180)
    obj.left(10)
