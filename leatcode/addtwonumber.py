# 2. Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.

l1=[2,4,3]
l2=[5,6,4]
l1.reverse()
l2.reverse()
out=[]
res1=0
res2=0
for i in l1:
    res1=res1*10+i
for j in l2:
    res2=res2*10+j
total=res1+res2
i=0
while total!=0:
    a=total%10
    out.append(a)
    total//=10
print(out)


    
