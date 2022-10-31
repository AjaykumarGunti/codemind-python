a=int(input())
def dig(v):
    s=0
    p=1
    for i in str(v):
        s+=int(i)
        p*=int(i)
    if s==p:
        return 'Spy Number'
    return 'Not Spy Number'
print(dig(a))