i=int(input())
sum=0
while i>0 or sum>9:
    if i==0:
        i=sum
        sum=0
    sum +=i%10
    i//=10
print(sum)
