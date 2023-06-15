n=int(input())
s=input()
alfa='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'
t=''
for i in range(len(s)):
  k=alfa.index(s[i])
  t+=alfa[k+n]
print(t)
