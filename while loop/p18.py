#extract the complex data items from the heterogenous list
l=eval(input("Enter the stirng:"))
i=0
list=[]
while i<len(l):
    if type(l[i])==complex:
        list.append(l[i])
    i+=1
print(list)