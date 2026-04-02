my_list=eval(input("Enter a list of numbers: "))
if len(my_list)%2!=0:
    if my_list[len(my_list)//2]>0:
        print(my_list[len(my_list)//2]+100)
    else:
        print("mid value is negative")
else:
    print('list has even number of elements')