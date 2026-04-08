#rev the give number
n=int(input("enter the number:"))
rev=0
while n!=0:
    a=n%10
    rev=a+(rev*10)
    n=n//10
print(rev)