#print the immutable data type 
t=eval(input("Enter the tupple:"))
for i in t:
    if type(i) not in [list,set,dict]:
        print(i)
    