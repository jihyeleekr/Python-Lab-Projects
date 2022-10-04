#Jihye Lee
#Time input from the user
time = int(input("Enter a total number of seconds:"))

#Convert the time from the user to hours, minutes, and seconds
hours = int(time//3600)
minuates = int((time%3600)/60)
seconds = int((time%3600)%60)

#Return the result
print(time,"seconds = ",hours,"hours",minuates,"minautes",seconds,"seconds")
