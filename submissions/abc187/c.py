n=int(input())
s={input() for _ in range(n)}
for i in s:
  if '!'+ i in s:
    print(i)
    exit()
else:
  print('satisfiable')
