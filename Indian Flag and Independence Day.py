import turtle

#background color
t = turtle.Turtle()
t.hideturtle()
s = turtle.Screen()
s.bgcolor("black")

#functions
def stage(x,y,col):
    t.penup()
    t.goto(x,y)
    t.color(col)
    t.pendown()

def rect(x,y):
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)
    t.fd(x)
    t.lt(90)
    t.fd(y)
    t.lt(90)
    
def flag(x, y, col):
    stage(x, y, "white")
    t.begin_fill()
    rect(80, 15)
    t.color(col)
    t.end_fill()

#drawing the stage
stage(-100, -150, "white")
rect(100, 20)

stage(-90, -130, "white")
rect(80, 20)

stage(-80, -110, "white")
rect(60, 20)

#drawing the pole
stage(-50, -90, "white")
t.begin_fill()
rect(4, 200)
t.color("white")
t.end_fill()

#drawing the tri-color flag  
flag(-46, 93, "#f4c430")
flag(-46, 78, "white")
flag(-46, 63, "green")

#drawing the circle
t.penup()
t.goto(-5, 78)
t.begin_fill()
t.circle(7)
t.color("blue")
t.end_fill()
t.pendown()

#writing independence wishes
t.penup()
t.goto(-150, 150)
t.color("green")
t.pendown()
t.write("Happy 74th Independence Day", font = ("Arial", 20, "normal"))

turtle.mainloop()
