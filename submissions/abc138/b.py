n=int(input())
a=list(map(int,input().split()))
count=0

for i in range(n):
  count+=float('{:.10f}'.format(1/a[i]))
print('{:.5f}'.format(1/count))
