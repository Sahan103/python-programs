#print the int from the give heterogenous list
m=eval(input("Enter the list:"))
i=0
while i<len(m):
    if type(m[i])==int:
        print(m[i])
    i+=1