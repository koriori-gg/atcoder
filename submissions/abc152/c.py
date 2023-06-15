n=int(input())
p=list(map(int,input().split()))
count=0
min=10**6
for i in range(n):
  if min>=p[i]:
    count+=1
    min=p[i]
print(count)
