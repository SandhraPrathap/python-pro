a=int(input("Enter the no. of elements "))
b=[]
sum=0
for x in range(a):
    try:
        b.append(int(input("Enter the element")))
    except ValueError:
        print("Value Error") 
for x in b:
    sum+=x         
print(b)
print(sum)    
