p,c,b,m,cs=map(int,input().split())
x=(p+c+b+m+cs)/5
if x>=90:
    print("Grade A")
elif x>=80:
    print("Grade B")
elif x>=70:
    print("Grade C")
elif x>=60:
    print("Grade D")
elif x>=40:
    print("Grade E")
else:
    print("Grade F")

