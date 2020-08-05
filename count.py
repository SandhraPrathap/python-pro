
a=input("Enter the string")
i=0
j=0
k=0
for x in a:
    if(x == 'a'or x=='A' or x=='e'or x=='E'or x=='i' or x=='I'or x=='o'or x=='O'or x=='u'or x=='U'):
        i+=1
    elif(x == ' '):
        j+=1
    else:
        k+=1
print("Vowels:",i)
print("Consonants:",k)
print("Spaces:",j)                