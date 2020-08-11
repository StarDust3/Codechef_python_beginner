n,m=map(float,input().split())
if n%5!=0:
    print(round(m,2))
elif n+0.5>m:
    print(round(m,2))
else:
    x=m-0.5-n
    print(round(x,2))