#Jihye Lee
def asks(ask):
    while ask == "Y" or ask == "YES" :
        hawaiian_Word_Pronouncer()
        
    while ask =="N" or ask == "NO":
        break
        
    while ask != "Y" or ask != "YES" or ask != "N" or ask != "NO":
        print("Enter Y, YES, N or NO")
        ask = str(input("Do you want to enter another word? Y/YES/N/NO ==> "))
        asks(ask)

def hawaiian_Word_Pronouncer():
    word = str(input("Enter a hawaiian word to pronounce ==>"))
    word  = word.lower()
    hawaiian_letter = ['a','e','i','o','u','p','k','h','l','m','n','w','’'," "]
    volws = {'a':'ah' , 'e':'eh', 'i':'ee', 'o':'oh' , 'u':'oo'}
    consonants = {'aw': 'w', 'uw': 'w', 'ow':'w', 'iw':'v', 'ew':'v'}
    catch = {'ai': 'eye', 'ae':'eye', 'ao': 'ow', 'au':'ow', 'ei':'ay', 'eu':'eh-oo', 'iu':'ew', 'oi':'oyo', 'ou':'ow', 'ui':'ooey'}
    pronounce = ""
    count = 0
    
    for letter in word:
        if letter not in hawaiian_letter:
            print(letter,"is not a valid hawaiian character")
            hawaiian_Word_Pronouncer()
        
    for l in range(0,len(word)):
        if count + 1 <= len(word)-1:
            tletter = " "
            tletter = word[count] + word[count+1]
                
            if word[0]=="w":
                pronounce = pronounce + 'w'
                    
            else:
                if tletter in consonants:
                    pronounce = pronounce + consonants[tletter]
                    count += 1
                    
                elif tletter in catch:
                    pronounce = pronounce + catch[tletter] +"-"
                    count += 1

                elif word[count] in volws:
                    pronounce = pronounce + volws[word[count]] +"-"

                    
                elif word[count] == '’' or word[count] == " ":
                    if pronounce[-1] == "-":
                        pronounce = pronounce[0:-1]
                        pronounce = pronounce + word[count]
                    else:
                        pronounce = pronounce +word[count]
                else:
                    pronounce = pronounce +word[count]
            count += 1
        else:
            tletter = " "
            tletter = word[count-2] + word[count-1]
            
            if tletter in catch or tletter in consonants:
                if pronounce[-1] == "-":
                    pronounce = pronounce[0:-1]
                    print(word.upper(), "is pronounced", pronounce.capitalize())
                    ask = str(input("Do you want to enter another word? Y/YES/N/NO ==> "))
                    ask.upper()
                    asks(ask)

                
            elif word[count] in volws:
                pronounce = pronounce + volws[word[count]] +"-"
                if pronounce[-1] == "-":
                    pronounce = pronounce[0:-1]
                    print(word.upper(), "is pronounced", pronounce.capitalize())
                    ask = str(input("Do you want to enter another word? Y/YES/N/NO ==> "))
                    ask.upper()
                    asks(ask)
                    
    
                else:
                    print(word.upper(), "is pronounced",pronounce.capitalize())
                    ask = str(input("Do you want to enter another word? Y/YES/N/NO ==> "))
                    ask.upper()
                    asks(ask)
                                
            else:
                pronounce = pronounce +word[count]
                print(word.upper(), "is pronounced", pronounce.capitalize())
                ask = str(input("Do you want to enter another word? Y/YES/N/NO ==> "))
                ask.upper()
                asks(ask)


