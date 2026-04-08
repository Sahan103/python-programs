#cehck the given number is amstrong or not
n=int(input("enter the number:"))
digit=len(str(n))
res=0
temp=n
while n!=0:
    id=n%10
    res+=(id**digit)
    n=n//10
if temp==res:
    print("amstrong")
else:
    print("not")


