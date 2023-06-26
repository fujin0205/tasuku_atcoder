n=int(input())
sum=0
d={}
for i in range(n):
  a=int(input())
  if a not in d:
    d[a]=1
  else:
    sum+=1
print(sum)