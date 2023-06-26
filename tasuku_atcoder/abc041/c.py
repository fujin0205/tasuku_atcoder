n=int(input())
l=input().split()
d={}
for i in range(n):
  d[l[i]] = i+1
  l[i] = int(l[i])
  
l.sort(reverse=True)
for i in range(n):
  print(d[str(l[i])])