#Jihye Lee

#Leap Year Function
def isLeapYear(year):
    if year % 4 !=0 :
        return False
    if year % 100 ==0:
        if year % 400 == 0:
            return True
        else:
            return False
    else:
        return True
    
#User Input
dates = input("Enter dates in MM/DD/YYYY order:")
date = dates.split('/')

#Month
month = date[0]
month = int(month)

#Days
days = date[1]
days = int(days)

#Years
years = date[2]
years = int(years)

#30 days months
if month in [4,6,9,11]:
        if days in range(1,31):
            print('Valid date')
        else:
            print("Invalid days")
            
#31 days months
elif month in [3,5,7,8,10,12]:
    if days in range(1,32):
        print('Valid date')
    else:
        print('Invalid days')
#Febuary
elif month ==2:
    if isLeapYear(years) == True:
        if days in range(1,30):
            print('Valid date')
        else:
            print('Invalid days')
    else:
        if days in range(1,29):
            print('Valid date')
        else:
            print('Invalid days, not a leap year.')
        
else:
    print('Invalid month')
    
    
    
