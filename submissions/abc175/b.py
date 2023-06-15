import itertools
n=int(input())
l=list(map(int,input().split()))
q=list(itertools.combinations(l,3))
count=0
for i in range(len(q)):
  if (q[i][0]!=q[i][1]) and (q[i][0]!=q[i][2]) and (q[i][1]!=q[i][2]) and (q[i][0]+q[i][1]>q[i][2]) and (q[i][1]+q[i][2]>q[i][0]) and (q[i][0]+q[i][2]>q[i][1]):
    count+=1
print(count)
