s=input()
n=len(s)
k=(n-1)//2
for i in range(k):
  if s[i]!=s[n-1-i]:
    print('No')
    exit()
else:
  for j in range(k//2):
    if s[j]!=s[k-1-j]:
      print('No')
      exit()
  else:
    print('Yes')
