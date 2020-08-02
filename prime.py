a=int(input("Enter the no."))
i=0
if(a==1):
    print("Neither prime nor composite")
else:    
    for x in range(2,a//2):
        if(a%x ==0):
            i=1
            break
        else:
            i=0
if(i==1):
    print("Not Prime")
else:
    print("Prime")            

        
