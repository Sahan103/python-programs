s='abbaca'
#o/p-->'ca'
out=[]
out.append(s[0])
for i in s[1::]:
    if out and i == out[-1]:
        out.pop()
    else:
        out.append(i)
print(''.join(out))
