import turtle as t
t.bgcolor('black')
t.speed(60)
t.pensize(1)
colors = ('magenta')
for i in range(200):
    t.forward(i*4)
    t.right(91)
    t.color(colors)
    for x in range(3):
        t.forward(x*4)
        t.right(91)
        for w in range(739):
            t.forward(w*4)
            t.right(891)
