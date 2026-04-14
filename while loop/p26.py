#sum of all odd numbers between the gievn range
n1=int(input("enter the number1:"))
n2=int(input("enter the number2:"))
i=n1
res=0
while i<=n2:
    if i%2!=0:
        res+=i
    i+=1
print(res)