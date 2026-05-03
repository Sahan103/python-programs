L=['hello',227,3.4,'last',189,34]
out=[]
for i in L:
    if type(i)==int:
        word=''
        for j in str(i):
            word=j+word
        out.append(int(word))
print(out)