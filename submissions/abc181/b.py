n=int(input())
count=0
for _ in range(n):
  a,b=map(int,input().split())
  count+=(b-a+1)*(b+a)//2
print(count)
