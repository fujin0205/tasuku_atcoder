import math
x1,y1,x2,y2,t,v=map(int,input().split())
n=int(input())
pos="NO"
for i in range(n):
  x,y=map(int,input().split())
  a1=math.sqrt((x1-x)**2+(y1-y)**2)
  a2=math.sqrt((x2-x)**2+(y2-y)**2)
  if t*v>=a1+a2:
    pos="YES"
  else:
    continue
print(pos)