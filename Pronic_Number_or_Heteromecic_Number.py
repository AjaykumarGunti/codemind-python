a=int(input())
s=0
for i in range(1,a):
    if i*(i+1)==a:
        s+=1
    else:
        s+=0
if s>0:
    print("YES")
else:
    print("NO")