n1=int(input())
n2=int(input())
i=1
hcf=1
while i<=n1 and i<=n2:
    if n1%i==0 and n2%i==0:
        if hcf<i:
            hcf=i
    i+=1
print(hcf)
