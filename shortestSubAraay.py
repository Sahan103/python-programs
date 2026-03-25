def shortestSubArray(n,target):
    for i in range(1,len(n)+1):
        for j in range(0,len(n)):
            if sum(n[j:j+i])==target:
                return len(n[j:j+i])
    return -1
num=[5,5,9,1]
t=15
a=shortestSubArray(num,t)
print(a)
       

