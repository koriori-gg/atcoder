n=int(input())
count=0
k=1
for i in range(1,n+1):
  if '7' in str(i) or '7' in oct(i):
    pass
  else:
    count+=1
print(count)
