d={'s':[1,2],'st':[1,2,3],'m':{1,2}}
#o/p {'s':[1,2]}
m={}
for i in d:
    if type(i)==str and len(i)==1:
        if type(d[i])==list and len(d[i])==2:
            m[i]=d[i]
print(m)
