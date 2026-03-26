#check the data is a single datatype or not
data=eval(input("Enter a data:"))
if type(data) in [int,float,complex,bool]:
    print("The data is a single value")