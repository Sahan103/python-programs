#wap ti toggle a string
s=input("enter a string:")
i=0
word=''
while i<len(s):
    if "A"<=s[i]<="Z":
        word+=chr(int(ord(s[i]))+32)
    elif "a"<=s[i]<="z":
        word+=chr(int(ord(s[i]))-32)
    elif "0"<=s[i]<="9":
        word+=s[i]
    else:
        word+=s[i]
    i+=1
print(word)