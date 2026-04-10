t=eval(input("Enter the stirng:"))
i=0
tuple=()
while i<len(t):
    if type(t[i])==str:
        if t[i][0] in 'AEIOUaeiou':
            tuple=tuple+(t[i],)
    i+=1
print(tuple)