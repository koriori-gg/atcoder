import collections
n=int(input())
s= list(input() for _ in range(n))
m=[]
point=0
c = collections.Counter(s)
m=c.most_common()
values, counts = zip(*c.most_common())
for i in range(len(values)):
  if counts[0] == counts[i]:
    point +=1
result= sorted(values[0:point])
for j in range(point):
  print(result[j])
