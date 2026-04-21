s='RCB CSK PBKS SRH DC'
#o/p 'RCB CSK SKBP CD'
list=s.split()
l=[]
for i in list:
    if len(i)%2==0:
        l.append(i[::-1])
    else:
        l.append(i)
res=' '.join(l)
print(res)