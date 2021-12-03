from turtle import *

t = Turtle()
# shape("turtle")
# t.shape("turtle")
tamanho = [1220, 600]

screen = Screen()
screen.bgcolor('black')

speed(25)
t.speed(5)

width(10)
setpos(-610, 300)
t.color('white')
color('green')
setpos(610, 300)
setpos(610, -300)
setpos(-610, -300)
setpos(-610, 300)

width(10)
for i in range(int(tamanho[1]/10)):
    forward(tamanho[0])
    if i % 2 == 0:
        right(90)
        forward(10)
        left(90)
    else:
        left(90)
        forward(10)
        right(90)

    right(180)

penup()
setpos(0, 0)
setpos(0, 270)

pendown()
color('yellow')
left(25)
width(5)

for i in range(156):
    i += 1
    right(50)
    forward(627.6-i*4)
    right(130)
    forward(627.6-i*4)
    right(50)
    forward(627.6-i*4)
    right(130)
    forward(627.6-i*4)

penup()
setpos(0, 0)
right(115)
pendown()

for i in range(50):
    penup()
    setpos(-150+i*3, 0)
    pendown()
    color('blue')
    width(10)
    circle(150-i*3)

penup()
setpos(-152, 5)
pendown()
left(115)
color('white')

width(7)
for i in range(795):
    right(0.4)
    forward(2)

    if i % 159 == 0 and i != 0:
        penup()
        setpos(-152, 5-(i/159*5))
        pendown()
        left(0.4*159)

t.fillcolor('white')
t.width(3)
t.penup()
t.setpos(75, -75)
t.pendown()
t.begin_fill()

for i in range(5):
    t.color('white')
    t.forward(20)
    t.right(144)

t.end_fill()

t.penup()
t.setpos(-5, 85)
t.pendown()
t.begin_fill()

for i in range(5):
    t.forward(20)
    t.right(144)

t.end_fill()

t.penup()
t.setpos(-10, -85)
t.pendown()
t.begin_fill()

for i in range(5):
    t.forward(20)
    t.right(144)

t.end_fill()

t.penup()
t.setpos(-80, -60)
t.pendown()
t.begin_fill()

for i in range(5):
    t.forward(20)
    t.right(144)

t.end_fill()

mainloop()
