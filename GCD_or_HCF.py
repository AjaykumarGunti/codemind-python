x,y=map(int,input().split())
s=0
for i in range(1,y+1):
    if x%i==0 and y%i==0:
        s=i
print(s)