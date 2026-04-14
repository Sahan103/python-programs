s='rcb mi dc csk'
#['rcb' 'mi' 'dc' 'csk']
i=0
out=[]
word=''
while i<len(s):
    if s[i]!=' ':
        word+=s[i]
    else:
        out.append(word)
        word=''
    i+=1
out.append(word)
print(out)