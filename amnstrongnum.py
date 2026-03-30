#check the given number is amstong or no
def amstrong(n):
    cube=len(str(n))
    res=0
    for i in str(n):
        m=int(i)**cube
        res+=m
    if res==n:
        return ('ammstorng')
num=153
print(amstrong(num))

