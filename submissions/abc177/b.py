s=input()
t=input()
s_len=len(s)
t_len=len(t)
n=s_len - t_len
max=0
for i in range(n+1):
  count=0
  for j in range(t_len):
    if s[j+i]==t[j]:
      count+=1
    if max<count:
      max=count
print(t_len - max)
