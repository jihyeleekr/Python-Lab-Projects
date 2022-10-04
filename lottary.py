import random

def megaMillion():
    nums = []
    
    for i in range(6):
        num = random.randint(1,70)
        nums += [num]

    if nums[0] ==nums[1]:
        nums[1] = random.choice(1,70)
        
    if nums[0] ==nums[2]:
        nums[2] = random.choice(1,70)

    if nums[0] ==nums[3]:
        nums[3] = random.choice(1,70)

    if nums[0] ==nums[4]:
        nums[4] = random.choice(1,70)
        
    if nums[0] ==nums[5]:
        nums[5] = random.choice(1,70)
        
    if nums[1] ==nums[2]:
        nums[2] = random.choice(1,70)
        
    if nums[1] ==nums[3]:
        nums[3] = random.choice(1,70)
        
    if nums[1] ==nums[4]:
        nums[4] = random.choice(1,70)
        
    if nums[1] ==nums[5]:
        nums[5] = random.choice(1,70)
        
    if nums[2] ==nums[3]:
        nums[3] = random.choice(1,70)
        
    if nums[2] ==nums[4]:
        nums[4] = random.choice(1,70)
        
    if nums[2] ==nums[5]:
        nums[5] = random.choice(1,70)
        
    if nums[3] ==nums[4]:
        nums[4] = random.choice(1,70)
        
    if nums[3] ==nums[5]:
        nums[5] = random.choice(1,70)
        
    if nums[4] ==nums[5]:
        nums[5] = random.choice(1,70)
    print("이번 로또 번호는:", nums, "입니다.")
    print("행운을 빌어요~")

def powerBall():
    nums = []
    
    for i in range(6):
        num = random.randint(1,69)
        nums += [num]

    if nums[0] ==nums[1]:
        nums[1] = random.choice(1,69)
        
    if nums[0] ==nums[2]:
        nums[2] = random.choice(1,69)

    if nums[0] ==nums[3]:
        nums[3] = random.choice(1,69)

    if nums[0] ==nums[4]:
        nums[4] = random.choice(1,69)
        
    if nums[0] ==nums[5]:
        nums[5] = random.choice(1,69)
        
    if nums[1] ==nums[2]:
        nums[2] = random.choice(1,69)
        
    if nums[1] ==nums[3]:
        nums[3] = random.choice(1,69)
        
    if nums[1] ==nums[4]:
        nums[4] = random.choice(1,69)
        
    if nums[1] ==nums[5]:
        nums[5] = random.choice(1,69)
        
    if nums[2] ==nums[3]:
        nums[3] = random.choice(1,69)
        
    if nums[2] ==nums[4]:
        nums[4] = random.choice(1,69)
        
    if nums[2] ==nums[5]:
        nums[5] = random.choice(1,69)
        
    if nums[3] ==nums[4]:
        nums[4] = random.choice(1,69)
        
    if nums[3] ==nums[5]:
        nums[5] = random.choice(1,69)
        
    if nums[4] ==nums[5]:
        nums[5] = random.choice(1,69)
        
    print("이번 로또 번호는:", nums, "입니다.")
    print("행운을 빌어요~")
        

    
def lotto ():
    print("Which one do you want to play?")
    print("1) Mega Million")
    print("2) Powerball")
    user = input("Please chose a number 1 or 2: ")
    user = int(user)
    
    if user == 1:
        megaMillion()
    
    elif user ==2:
        powerBall()
