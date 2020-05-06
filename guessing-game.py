import random
print("Number game")
start=0
end=20
computernumber=random.randint(0,20)
while(True):
    usernumber= int(input("enter the number:"))
    if usernumber == computernumber:
        print("your number is correct")
        break
    elif usernumber > computernumber:
         end=computernumber
         midpoint=(start+end/2)
         print(midpoint)
         if(midpoint>usernumber):
            print("your number is high")
         else:
             print("your number is too high")
    elif usernumber<computernumber:
         end=usernumber
         midpoint=(start+end/2)
         print(midpoint)
         if(midpoint<computernumber):
            print("your number is low")
         else:
              print("your number is too low")

    else:
                print("invalid")