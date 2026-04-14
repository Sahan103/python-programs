#by using while loop check the given number is prime or not
n=int(input("enter a number:"))
i=1
count=0
while i<=n:
    if n%i==0:
        count+=1
    i+=1
if count==2:
    print("prime")
else:
    print('not a prime')