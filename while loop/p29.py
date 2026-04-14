n=int(input("Enter the number:"))
res=0
temp=n
while n!=0:
    a=n%10
    res=a+(res*10)
    n=n//10
print(res)
if res==temp:
    print("palindrome")
else:
    print("not a palindrome")