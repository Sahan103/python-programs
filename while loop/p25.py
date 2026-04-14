#remove the duplicates from list
n=eval(input("enter the list"))
i=0
list=[]
while i<len(n):
    if n[i] not in list:
        list.append(n[i])
    i+=1
print(list)