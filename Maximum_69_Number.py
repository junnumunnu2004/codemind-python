n=input()
L=[]
for i in n:
    L.append(int(i))
for i in range(len(n)):
    if (L[i]==6):
        L[i]=9
        break
n=""
for i in L:
    n=n+str(i)
print(n)
        