from turtle import *
speed(25)
color('cyan')
bgcolor('black')
b = 200
setpos(300, 10)
while b > 0:
    left(b)
    forward(b * 3)
    b = b - 1
