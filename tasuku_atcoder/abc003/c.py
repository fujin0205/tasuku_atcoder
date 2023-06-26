x=str(input())
y=str(input())
n=len(x)
result="win"
at={"a","t","c","o","d","e","r"}
 
for i in range(n):
  if x[i]=="@" and y[i] in at:
    continue
  elif y[i]=="@" and x[i] in at:
    continue
  elif x[i]==y[i]:
    continue
  else:
    result="lose"
    break
if result=="win":
  print("You can win")
else:
  print("You will lose")