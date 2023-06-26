n=int(input())
l=list(map(int, input().split()))
ans=[]
for j in range(min(l),max(l)+1):
  ans += [sum([(i-j)**2 for i in l])]
  
print(min(ans))
  