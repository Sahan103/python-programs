#extract the lower case letter from the string
s=input("Enter the stirng:")
i=0
lower=''
while i<len(s):
    if 'a'<=s[i]<='z':
        lower=lower+s[i]
    i+=1
print(lower)