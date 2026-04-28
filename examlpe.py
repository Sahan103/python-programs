m=[3,-5,8,9,1,-4,10]
long=[]
for i in range(1,len(m)):
    for j in range(len(m)):
        count=0
        for c in m[j:j+i]:
            if c>0:
                count+=1
        if len(long)<count:
            long=m[j:j+i]
print(long)