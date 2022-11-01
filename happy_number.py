a=int(input())
b=0
while a>0 or b>9:
    if a==0:
        a=b
        b=0
    b+=(a%10)**2
    a=a//10
if b==1 or b==7:
    print("True")
else:
    print("False")