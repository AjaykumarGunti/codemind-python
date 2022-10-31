a=int(input())
def digit(n):
    s=0
    for i in (str(n)):
        s+=int(i)
    return s
while digit(a)>9:
    a=digit(a)
print(digit(a))