#Jihye Lee
import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()



my_turtle.shape("turtle")
for _ in range(12):
    my_turtle.penup()
    my_turtle.forward(65)
    my_turtle.pendown()
    my_turtle.forward(5)
    my_turtle.penup()
    my_turtle.forward(15)
    my_turtle.stamp()
    my_turtle.forward(-85)
    my_turtle.right(30)
    
