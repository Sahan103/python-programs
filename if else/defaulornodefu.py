#given data default or not
data=eval(input("enter data:"))
if bool(data) in (True,False):
    print("given data is default")
else:
    print("given data is not default")