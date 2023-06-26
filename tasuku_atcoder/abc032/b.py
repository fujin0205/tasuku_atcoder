s=input()
d={}
k=int(input())
count=0
for i in range(len(s)+1-k):
  if s[i:i+k] not in d.keys():
    count+=1
    d[s[i:i+k]]=1
print(count)