import turtle
t= turtle.Turtle()
s= turtle.Screen()
t.hideturtle()
s.bgcolor("black")
t.penup()
t.goto(-100,-100)
t.color("white")
t.begin_fill()
t.pendown()
dist = [140,95,140]
for i in range(3):
    t.fd(dist[i])
    t.lt(90)
t.fd(95)
t.end_fill()

x = -120
dx = 30
colors = ["red", "blue", "green", "yellow", "orange", "violet", "indigo"]
t.lt(180)
for i in range(5):
    t.penup()
    x += dx
    t.goto(x, 0)
    t.color(colors[i])
    t.pendown()
    t.fd(20)

t.penup()
t.goto(-40,-50)
t.pendown()
for each_color in colors:
    angle = 360 / len(colors)
    t.color(each_color)
    t.circle(10)
    t.rt(angle)
    t.fd(10)

t.penup()
t.goto(-150,50)
t.color("white")
t.pendown()
t.write("    Happy Birthday", move=False, align='left', font=('Arial', 20, 'normal'))
turtle.mainloop()
