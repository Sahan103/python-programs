#print if the given string character is upperecase and multiple of 3
s=(input("enter the number:"))
i=0
while i<len(s):
    if 'A'<=s[i]<='z' and ord(s[i])%3==0:
        print(s[i])
    i+=1