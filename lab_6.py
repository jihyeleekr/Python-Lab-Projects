#Jihye Lee
def mario():
    height = int(input("Height: "))
    count = height
    
    while height<1 or height>8:
        height = int(input("Height: "))
        
    for i in range(height+1):
       
        print("  " *count, end = " ")
        print("#"*i, end = " ")
        
        print("  ", end = " ")
        print("#" *i)
        count = count -1
        

def credit():
    numbers = input("Number:")
    numbers = str(numbers)
    numset = []
    sum1 = 0
    sum2 =0

#Visa
    if len(numbers) == 16 and numbers[0] == "4" or len(numbers) ==13 and numbers[0] == "4":
        print("Visa")
        for _ in range(16):
            numset.append(numbers[:1])
            numbers = numbers[1:]
        
        for i in range(0,16,2):
            if int(numset[i])*2 >= 10:
                sum1 = sum1 + 1 + (int(numset[i])*2-10)
                
            else:
                sum1 = sum1 +int(numset[i])*2

        for j in range(1,16,2):
            sum2 = sum2 + int(numset[j])
        
        sum2 = sum2 +sum1
        
        if sum2 % 10 == 0:
            print( 'Vaild')
        else:
            print("Invalid")
            
#America Express
    if len(numbers) == 15:
        if numbers[0] == "3":
            if numbers [1] =="4" or numbers[1] == "7":
                
                print("America Express")
                for _ in range(16):
                    numset.append(numbers[:1])
                    numbers = numbers[1:]
        
                for i in range(0,15,2):
                    sum1 = sum1 +int(numset[i])*2
        
                for j in range(1,15,2):
                    sum2 = sum2 + int(numset[i])
        
                sum2 = sum2 +sum1
        
        
                if 10 %sum2 == 0:
                    print("Vaild")
                else:
                   print("Invalid")
                   
#MasterCard
    if len(numbers) == 16:
        if numbers[0] == "5":
            if numbers[1] =="1" or numbers[1] =="2" or numbers[1] =="3" or numbers[1] =="4" or numbers[1] =="5":
                    print("MasterCard")
                    for _ in range(16):
                        numset.append(numbers[:1])
                        numbers = numbers[1:]
        
                    for i in range(0,16,2):
                        sum1 = sum1 +int(numset[i])*2
                
                    for j in range(1,17,2):
                        sum2 = sum2 + int(numset[i])
        
                    sum2 = sum2 +sum1
                    
                    if 10 %sum2 == 0:
                        print("Vaild")
                    else:
                       print("Invalid")
    
   
   
