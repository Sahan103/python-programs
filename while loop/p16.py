#add all the ASCII value of the given string
s=input('enter the string:')
i=0
res=0
while i<len(s):
    res+=ord(s[i])
    i+=1
print(res)