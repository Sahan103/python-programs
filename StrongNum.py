def st_num(n):
    res=0
    if n>=1:
        for i in str(n):
            m=int(i)
            fact=1
            j=1
            while j<=m:
                fact=fact*j
                j+=1
            res+=fact
        return res==n
    else:
        return -1
n=-145
a=st_num(n)
print(a)
