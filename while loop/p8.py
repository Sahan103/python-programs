#CHECK THE GIVEN NUMBER IS PERFECT,DEFECIENT OR ABONDENT
n=int(input("enter the number:"))
i=1
res=0
while i<n:
    if n%i==0:
        res+=i
    i+=1
if res==n:
    print("perfect")
elif res<n:
    print("defecient")
else:
    print("abondant")