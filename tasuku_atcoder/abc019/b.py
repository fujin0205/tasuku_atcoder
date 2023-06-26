sen=str(input())
count=0
word=sen[0]
for i in range(len(sen)):
  if sen[i]==word:
    count+=1
  else:
    print(word+str(count),end="")
    word=sen[i]
    count=1
  if i==len(sen)-1:
    print(word+str(count))