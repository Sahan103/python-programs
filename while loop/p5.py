#add all the digit of the give numbers
n=int(input("enter the number:"))
res=0
while n!=0:
    a=n%10
    res+=a
    n=n//10
print(res)