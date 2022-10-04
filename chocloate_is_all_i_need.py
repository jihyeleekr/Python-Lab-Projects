# Input from the user
height = float(input("Enter your height in inches:"))
weight = float(input("Enter your weight in pounds:"))
age = int(input("Enther your age in years:"))

#BMR calculation for Woman and Man
bmrw = 655.1 + (4.35*weight) + (4.7*height) -(4.7* age)
bmrw = int(bmrw)
bmrw = int(bmrw/214)

bmrm = 66+(6.2*weight)+(12.7*height)-(6.76*age)
bmrm = int(bmrm)
bmrm = int(bmrm/214)

#Output for each gender
print("If you are a woman, you have to consume", bmrw,"choclate bars.")
print("If you are a man, you have to consume", bmrm,"choclate bars.")
