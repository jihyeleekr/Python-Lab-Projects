import turtle

nw = turtle.Screen()

myturtle = turtle.Turtle()

for _ in range(3):
    myturtle.forward(100)
    myturtle.left(120)
    
myturtle.forward(50)
myturtle.left(120)
myturtle.forward(50)
for _ in range(2):
    myturtle.right(120)
    myturtle.forward(50)

