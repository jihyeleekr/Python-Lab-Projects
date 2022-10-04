#Jihye Lee
def bottle_of_beer(n):
    for i in range(n):
        print(n, "bottles of beer on the wall," ,n,"bottles of beer")
        print("Take one down, pass it around,", end =' ')
        n = n-1
        print(n, "bottles of beer on the wall")
        print()

def multiplication_table(n):
    for i in range(n):
        for j in range(n):
            print((i+1)*(j+1), end = "   ")
        print()

def summation_of_squares(n):
    total =0
    for i in range(n):
        nsq = n**2
        n = n-1
        total = total +nsq
    print(total)

import turtle
myTurtle = turtle.Turtle()
my_screen = turtle.Screen()
myTurtle.speed(20)

def drawSquare(myTurtle, squareSize):
    for i in range(4):
        myTurtle.forward(squareSize)
        myTurtle.left(90)

def drawRow(myTurtle, length, squareSize):
    for i in range(length):
        drawSquare(myTurtle, squareSize)
        myTurtle.forward(squareSize)
        
def drawGrid(myTurtle, size, squareSize):
    for i in range(size):
        length = size
        drawRow(myTurtle, length, squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize*length)
        myTurtle.right(180)

def drawSquareStairs(myTurtle, height, squareSize):
    length = height
    for i in range(height):
        drawRow(myTurtle, length, squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize)
        myTurtle.left(90)
        myTurtle.forward(squareSize*length)
        myTurtle.right(180)
        length -= 1

def drawNgon(myTurtle, numSides, sideLength):
    for _ in range(numSides):
        myTurtle.forward(sideLength)
        myTurtle.left(360/numSides)
        
def drawNgonSpiral(myTurtle, numSides, sideLength, numShapes):
    for i in range(numShapes):
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.left(720/numShapes)
        

#Top part of hourglass
def hourGlassTop(x):
    print("|", end = " ")
    for i in range(0,10):
        print('"', end = " ")
    print("|")

    for j in range(4):
        print(" ", end = " ")
        
        for _ in range(0,j):
            print(" ", end = " ")
        print("\\", end = " ")
        
        for _ in range(x):
            print(":", end = " ")
        x = x-2
        print("/")

#Middle part of hourglass
def hourGlassMiddle():
    for i in range(5):
        print(" ", end = " ")
    print("||")

 #Bottom part of hourglass
def hourGlassBottom(y,z):
    for i in range(4):
        for _ in range(z):
            print(" ", end = " ")
        print("/", end = " ")
        z = z-1
        
        for _ in range(y):
            print(":", end = " ")
        y = y+2
        print("\\")
        
    print("|", end = " ")
    for j in range(0,10):
        print('"', end = " ")
    print("|")
        
#HourGlass
def hourGlass():
    hourGlassTop(8)
    hourGlassMiddle()
    hourGlassBottom(2,4)


def slashFigure(n):
    figure = int(4*n - 2)
    row = int(n)
    slash1 = 0
    slash2 = 0
    for i in range(row):
        
        for _ in range(slash1):
            print("\\", end = " ")
        slash1 = slash1 + 2
        
        for _ in range(figure):
            print("!", end = " ")
        figure = figure - 4

        for _ in range(slash2):
            print("/", end =" ")
        slash2 = slash2 + 2
        
        print(" ")




def superDuperSprial(myTurtle, numSides, sideLength, numShapes):
    colors = ['aquamarine3', 'IndianRed1', 'LightSlateBlue', 'seashell1', 'PaleGreen3', 'RosyBrown2', 'orchid2', 'OliveDrab4', 'PeachPuff']
    
    for i in range(numShapes):
        myTurtle.color(colors[i%9])
        drawNgon(myTurtle, numSides, sideLength)
        myTurtle.left(720/numShapes)
        
        
    


        
        
        
    
        
        
        
        
        
        
        
    
            

    
