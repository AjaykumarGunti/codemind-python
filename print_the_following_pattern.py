a=int(input())
for row in range(a):
    for col in range(a):
        if row==col:
            print("0",end="")
        else:
            print("x",end="")
    print()