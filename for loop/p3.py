#print integer data items only
s=eval(input("enter the set:"))
for i in s:
    if type(i)==int:
        print(i)