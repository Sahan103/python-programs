s='kabab is love'
out={}
for i in s.split():
    count=0
    for j in i:
        if j in 'aeiouAeiou':
            count+=1
    out[i]=[i[::-1],count,i[0::2]]
print(out)
   


