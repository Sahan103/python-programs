#print the immutable dataitems form the heterogenous tuple
t=eval(input("enter the heterogenous tuple:"))
i=0
while i<len(t):
    if type(t[i]) not in [list,set,dict]:
        print(t[i])
    i+=1