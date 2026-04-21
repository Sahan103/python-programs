m=[25,346,-33,105,78,-89]
#[25,33,78,89]
out=[]
for i in m:
    num=abs(i)
    if 10<=num<=99:
        out.append(num)
print(out)