s='kabab is love'
out={}
for i in s.split():
    cons=''
    for j in i:
        if j not in 'aeiouAEIOU':
            cons+=j
    out[i[0]+i[-1]]=[cons,len(cons),cons[::-1]]
print(out)