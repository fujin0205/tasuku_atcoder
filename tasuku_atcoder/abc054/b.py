n,m=map(int,input().split())
a=[input() for i in range(n)]
b=[input() for i in range(m)]
for i in range(n-m+1):
  for j in range(n-m+1):
    if [s[j:j+m] for s in a[i:i+m]]==b:
      print("Yes")
      exit()
print("No")