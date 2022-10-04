#Jihye Lee
import turtle

my_turtle =turtle.Turtle()
my_screen = turtle.Screen()

my_turtle.pensize(10)
#Get an input from the user
n = input("Enter the number of sides you like:")
n = int(n)

angle = 360/n

#Use for Loop
for _ in range(n):
    my_turtle.forward(60)
    my_turtle.left(angle)

