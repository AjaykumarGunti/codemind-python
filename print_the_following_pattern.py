a=int(input())
for i in range(a):
    for j in range(a):
        if i==j or (j==0 and i!=0) or (j==a-1 and i!=a-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()