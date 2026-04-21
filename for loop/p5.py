#print the values if the key is str and values is mutable
d=eval(input("Enter the dict:"))
for i in d:
    if type(i)==str and type(d[i]) in [list,set,dict]:
        print(d[i])