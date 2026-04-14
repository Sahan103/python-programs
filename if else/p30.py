s=input("enter the binary values:")
#100
i=len(s)-1 #2
j=0
res=0
while i>=0:
    a=int(s[i])
    res=res+(a*(2**j))
    i-=1
    j+=1
print(res)