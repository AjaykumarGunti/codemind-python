x,y,z=map(int,input().split())
s=((x+y+z)/2)
b=(s*(s-x)*(s-y)*(s-z))
a=b**0.5
f="{:.2f}".format(a)
print(f)