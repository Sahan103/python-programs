L=[100,200,50,400,300]
target=300
for i in L:
    for j in L:
        if i+j==target:
            out=[[i,j],[target]]
            break
    if out:
        break
print(out)