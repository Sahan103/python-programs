#print the devisor of the give number
n=int(input("enter the number:"))
i=1
while i<n:
    if n%i==0:
        print(i)
    i+=1
    