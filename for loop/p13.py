s='ab3cba33bs'
#o/p-->{'a':2,'b':3,'3':4,'c':1}
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(d)