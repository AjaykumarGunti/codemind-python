a=int(input())
for row in range(a):
    for col in range(a):
        if row==col or row+col==a-1 :
            print("x",end='')
        else:
            print("0",end='')
    print()