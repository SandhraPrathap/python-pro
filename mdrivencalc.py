print("Enter 2 numbers")
a=int(input())
b=int(input())
c=int(input("Enter 1-sum,2-subtraction,3-multiplication,4-product"))
if(c==1):
    sum=a+b
    print("Sum :",sum)
    
elif(c==2):
    sum=a-b
    print("Difference:",sum)
    
elif(c==3):
    sum=a*b
    print("Product:",sum)
    
elif(c==4):
    sum=a/b
    print("Quotient:",sum)
    
else:
    print("Invalid input")
    