#add all the devisor of the given number
n=int(input("enter the number:"))
i=1
res=0
while i<n:
    if n%i==0:
        res+=i
    i+=1
print(res)