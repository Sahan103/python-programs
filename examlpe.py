n=input()
i=0
while i<len(n):
    if 'A'<=n[i]<='Z' and ord(n[i])%3==0:
        print(n[i])
    i+=1