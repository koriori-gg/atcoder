n=int(input())
s=input()
count=0
for _ in range(20):
  f=len(s)
  s=s.replace('ABC','',1)
  if len(s)!=f:
    count+=1
print(count)
