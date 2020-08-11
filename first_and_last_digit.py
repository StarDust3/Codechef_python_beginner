n=int(input())
for i in range(n):
    d=int(input())
    e=d%10
    gf=len(str(d))
    f=d//(10**(gf-1))
    print(f+e)