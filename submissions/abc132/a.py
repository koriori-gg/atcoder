s=list(input())
s.sort()

if s[0]==s[1] and s[2]==s[3]:
  if s[0]!=s[3]:
    print('Yes')
  else:
    print('No')
else:
  print('No')
