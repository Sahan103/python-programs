#print the vowel letters of the given string
s=(input("enter the number:"))
i=0
while i<len(s):
    if s[i] in 'AEIOUaeiou':
        print(s[i])
    i+=1