#the given to integer is happy if any one is equal to 10 or sum of two integer is 10 otherwiawse sad
num1=int(input("enter first number:"))
num2=int(input("enter second number:"))
if num1==10 or num2==10 or num1+num2==10:
    print("happy")  
else:   
    print("sad")