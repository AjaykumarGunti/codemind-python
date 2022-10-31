a=int(input())
b=list(map(int,input().split()))
s=0
for i in range(a):
    if i%2==1:
        s+=b[i]
print(s)