x,y=(int(x) for x in input().split())
x = x%12
short=30*x+y*0.5
long=6*y
diff=abs(short-long)
if diff>180:
  diff=abs(360-diff)
print(diff)