#Jihye Lee
def main():
    print("It’s time to go on a scavenger hunt!")
    print("You'd be amazed how many things can go wrong!")
    time = input("Please enter how long you want to travel for:")
    initialPos = 7.0;
    time = float(time);
    velocity = 5.0;
    acceleration = 1.0;
    # there is a math error in here causing
    # an incorrect answer in the line below
    position = initialPos + velocity * time + (1 / 2) *acceleration*(time**2);
    #if you are stuck on the math error, look at the footnote
    print(position);
main()
