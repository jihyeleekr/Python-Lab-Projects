#Jihye Lee
import turtle


def irma_setup():
    """Creates the Turtle and the Screen with the map background
       and coordinate system set to match latitude and longitude.

       :return: a tuple containing the Turtle and the Screen

       DO NOT CHANGE THE CODE IN THIS FUNCTION!
    """
    import tkinter
    turtle.setup(965, 600)  # set size of window to size of map

    wn = turtle.Screen()
    wn.title("Hurricane Irma")

    # kludge to get the map shown as a background image,
    # since wn.bgpic does not allow you to position the image
    canvas = wn.getcanvas()
    turtle.setworldcoordinates(-90, 0, -17.66, 45)  # set the coordinate system to match lat/long

    map_bg_img = tkinter.PhotoImage(file="images/atlantic-basin.png")

    # additional kludge for positioning the background image
    # when setworldcoordinates is used
    canvas.create_image(-1175, -580, anchor=tkinter.NW, image=map_bg_img)

    t = turtle.Turtle()
    wn.register_shape("images/hurricane.gif")
    t.shape("images/hurricane.gif")

    return (t, wn, map_bg_img)


def irma():
    """Animates the path of hurricane Irma
    """
    (t, wn, map_bg_img) = irma_setup()

    # your code to animate Irma here
    x = []
    y = []
    wind = []

    t.speed(0)
    file = open('irma.csv','r')
    read = file.readlines()[1::]
    
    for i in read:
        data = i.split(",")
        x.append(float(data[3]))
        y.append(float(data[2]))
        wind.append(int(data[4]))
        
    for j in range(0,len(read)-1):
        
        t.penup()
        t.goto(x[j],y[j])
        
        if wind[j] >= 74 and wind[j] <= 95:
            t.pensize(2)
            t.pendown()
            t.color("Blue")
            t.write(1)
            t.goto(x[j+1],y[j+1])
            
        elif wind[j] >= 96 and wind[j] <=110:
            t.pensize(4)
            t.pendown()
            t.color("Green")
            t.write(2)
            t.goto(x[j+1],y[j+1])
            
        elif wind[j] >= 111 and wind[j] <= 129:
            t.pensize(6)
            t.pendown()
            t.color("Yellow")
            t.write(3)
            t.goto(x[j+1],y[j+1])
            
        elif wind[j] >= 130 and wind[j] <= 156:
            t.pensize(8)
            t.pendown()
            t.color("Orange")
            t.write(4)
            t.goto(x[j+1],y[j+1])
            
        elif wind[j] >= 157:
            t.pensize(10)
            t.pendown()
            t.color("Red")
            t.write(5)
            t.goto(x[j+1],y[j+1])
            
        else:
            t.pensize(1)
            t.pendown()
            t.color("White")
            t.goto(x[j+1],y[j+1])
            
    wn.exitonclick()
if __name__ == "__main__":
    irma()
