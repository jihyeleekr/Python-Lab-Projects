import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()


my_turtle.pensize(5)

my_turtle.penup()
my_turtle.goto(0,0)
my_turtle.pendown()
#Blue Ring
my_turtle.color("blue")
my_turtle.circle(25)

my_turtle.penup()
my_turtle.forward(60)
#Black Ring
my_turtle.down()
my_turtle.color("black")
my_turtle.circle(25)

my_turtle.penup()
my_turtle.forward(60)
#Red Ring
my_turtle.pendown()
my_turtle.color("red")
my_turtle.circle(25)

my_turtle.up()
my_turtle.forward(-5)
my_turtle.right(90)
my_turtle.forward(4)
#Green Ring
my_turtle.down()
my_turtle.color("green")
my_turtle.circle(-25, 246)
my_turtle.up()
my_turtle.forward(10)
my_turtle.right(10)
my_turtle.right(90)
my_turtle.forward(0.6)
my_turtle.left(90)

my_turtle.forward(0.9)
my_turtle.down()
my_turtle.circle(-20.5,98.5)

my_turtle.up()
my_turtle.goto(55,0)
my_turtle.forward(4)
#Yellow Ring
my_turtle.down()
my_turtle.color("yellow")
my_turtle.circle(-25, 246)
my_turtle.up()
my_turtle.forward(10)
my_turtle.right(10)
my_turtle.right(90)
my_turtle.forward(0.6)
my_turtle.left(90)

my_turtle.forward(0.9)
my_turtle.down()
my_turtle.circle(-20.5,98.5)







                



