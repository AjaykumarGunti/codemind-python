n=int(input())
sqr=n**2
sum=0
while sqr>0:
    dig=sqr%10
    sum=sum+dig
    sqr=sqr//10
if sum==n:
    print("Neon Number")
else:
    print("Not Neon Number")