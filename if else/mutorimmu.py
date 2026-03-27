#given data is mutable or immutable
data=eval(input("enter data:"))
if type(data) in (int,float,bool,complex,str,tuple):
    print("given data is immutable")
else:
    print("given data is mutable")