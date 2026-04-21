#print all the uppercase and the ascivalue is devisible by 3
s=input("enter the string:")
for i in s:
    if 'A'<=i<='Z' and ord(i)%3==0:
        print(i)