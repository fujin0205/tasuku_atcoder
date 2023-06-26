n=int(input())
c,s,d=0,0,0
for i in range(n):
    x,y=map(int,input().split())
    if c==0:
        if y>0:
            c=x
            s+=y
            d=0
    else:
        if x==1 and d<y:
            s=s+y-d
            d=y
        elif x==0:
            s+=y
            c=x
print(s)
