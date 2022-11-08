for i in range(int(input())):
    b=input()
    c=list(map(int,input().split()))
    if c==sorted(c):
        print("0")
    else:
        print(max(c)-min(c))