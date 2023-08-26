a=int(input())  
sum_v=0  
for i in range(1,a):  
    if (a%i==0):  
        sum_v=sum_v+i  
if(sum_v==a):  
    print("True")  
else:  
    print("False")