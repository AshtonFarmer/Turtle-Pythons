import turtle
a = turtle.Turtle()
s = turtle.Screen()
s.bgcolor('black')
col = ("white", "red", "orange", "yellow","green", "blue", "cyan")
a.speed(0)

for i in range(200):
    a.forward(i*4)
    a.right(91)
    a.color(col[i%7])  # just this is a blackhole box
    for b in range(3): #adding this makes vortex
        a.forward(i*4)
        a.right(91)
        for c in range(2): # puzzle piece vortex?
            a.forward(i*4)
            a.left(91)
            