def Diseram_num(n):
    res=0
    m=str(n)
    for i in range(len(m)):
        s=int(m[i])
        cube=s**(i+1)
        res+=cube
    return res==n
num=89
print(Diseram_num(num))