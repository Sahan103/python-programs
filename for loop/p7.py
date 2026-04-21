s='ab cde  fg'
#o/p 'ab&cde&&fg'
out=''
for i in s:
    if i!=' ':
        out=out+i
    else:
        out=out+'&'
print(out)

