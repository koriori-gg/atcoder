a=[int(i) for i in input()]
n=len(a)-1
for i in range(2**n):
  answer=str(a[0])
  total=a[0]
  for j in range(n):
    if ((i>>j)&1):
      answer+='+'
      total+=a[j+1]
      answer+=str(a[j+1])
    else:
      answer+='-'
      total-=a[j+1]
      answer+=str(a[j+1])
  if (total==7):
    answer+='=7'
    print(answer)
    exit()
