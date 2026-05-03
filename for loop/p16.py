s='bacbcaabbaa'
out=''
for i in range(len(s)):
    count=1
    if s[i] not in out:
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                count+=1
        out=out+s[i]+str(count)
print(out)