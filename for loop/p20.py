n=int(input("Enter a number:"))
res=0
for i in str(n):
    m=int(i)
    fact=1
    for j in range(1,m+1):
        fact*=j
    res+=fact
if n==res:
    print("strong")
else:
    print("not a strogn")