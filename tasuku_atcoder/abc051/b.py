k,s=list(map(int,input().split()))
ans=0
for i in range(k+1):
  for j in range(k+1):
    z=s-i-j
    if z>=0 and z<=k:
      ans+=1
print(ans)