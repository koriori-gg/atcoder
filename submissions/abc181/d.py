from collections import Counter
s=input()

if len(s)<=2:
  if int(s)%8==0 or int(s[::-1])%8==0:
    print('Yes')
    exit()
  else:
    print('No')
    exit()

c=Counter(s)

for i in range(104,1000,8):
  if not Counter(str(i)) - c:
    print("Yes")
    exit()

print("No")
