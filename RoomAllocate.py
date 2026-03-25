def roomAllocate(h,c):
    for i in h:
        for j in c:
            if j>=i:
                c.remove(j)
                break
    return len(c)
h=[20,3,30,7,15]
c=[8,25,5,18,9]
b=roomAllocate(h,c)
print(b)