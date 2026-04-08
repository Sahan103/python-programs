#greatest of 3 number using nested if 
a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))  
if a>c:
    if a>b:
        print(a,"is the greatest number")
    else:
        print(b,"is the greatest number")
elif c>b:
    print(c,"is the greatest number")
else:    
    print(b,"is the greatest number") 