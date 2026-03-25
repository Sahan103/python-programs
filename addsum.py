def sum_in(n):
    res=0
    if n>=1:
        for i in str(n):
            m=int(i)
            res+=m
        return res
    else:
        return -1
print(sum_in(-23))