s=list(input())
for i in range(4):
  k=s[i:i+3]
  if k==['o','o','o']:
    print('o')
    exit()
  elif k==['x','x','x']:
    print('x')
    exit()
else:
  print('draw')
