m=[20,40,60,80,90]
#o/p-->[270,250,230,210,200]
res=sum(m)
for i in range(len(m)):
    m[i]=res-m[i]
print(m)