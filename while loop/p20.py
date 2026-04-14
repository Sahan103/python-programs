s='ABCxyZ12M'
#o/p ---.['ABC','xy','Z','12','M']
i=0
out=[]
word=''
while i<len(s)-1:
    if ord(s[i])+1==ord(s[i+1]):
        word+=s[i]
    else:
        word+=s[i]
        out.append(word)
        word=''
    i+=1
word+=s[i]
out.append(word)
print(out)