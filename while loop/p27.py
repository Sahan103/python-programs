#greatest of the given numbetr
list=eval(input("enter the list og integer:"))
i=0
great=list[i]
while i<len(list):
    if great<list[i]:
        great=list[i]
    i+=1
print(great)