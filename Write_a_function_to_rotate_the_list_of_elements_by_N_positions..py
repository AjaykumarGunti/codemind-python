a=int(input())
b=list(map(int,input().split()))
c=int(input())
for i in range(1,c+1):
    k=b[-i]
    b.insert(0,k)
print(*(b[:-c]))