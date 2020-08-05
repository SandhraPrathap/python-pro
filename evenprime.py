a=int(input("Enter the no."))
print("Enter 1 to check if prime or not and 2 to check if even or odd")
b=int(input())
if(b==1):
    i=0
    if(a==1):
        print("Neither prime nor composite")
    else:    
        for x in range(2,a//2):
            if(a%x ==0):
                i=1
                break
            
    if(i==1):
        print("Not Prime")
    else:
        print("Prime") 
elif(b==2):
    if(a%2==0):
        print("Even")
    else:
        print("Odd")
else:
    print("Invalid input")                    
