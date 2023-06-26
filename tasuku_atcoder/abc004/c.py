n=int(input())%30
a=[i for i in range(1,7)]
c=0
for i in range(n):
  k=i%5
  v=i%5+1
  a[k],a[v]=a[v],a[k]
print("".join(map(str,a)))