#extract all the even integer in a tuple at odd index
t=eval(input("enter the tuple:"))
i=0
l=[]
while i<len(t):
    if t.index(t[i])%2!=0 and t[i]%2==0:
        l+=[t[i]]
    i+=1
print(l)