def amstrong(n):
    cube=len(str(n))
    res=0
    for i in str(n):
        m=int(i)**cube
        res+=m
    if res==n:
        return ('amms')
num=153
print(amstrong(num))

