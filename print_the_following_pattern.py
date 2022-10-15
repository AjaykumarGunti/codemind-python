a=int(input())
for row in range(a):
    for col in range(a):
        if row==col or (row!=0 and col==0) or (row==a-1 and col!=a-1):
            print("*",end="")
        else:
            print(" ",end="")
    print()