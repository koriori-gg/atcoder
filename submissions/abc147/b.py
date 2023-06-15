s=input()
l=len(s)
count=0
for i in range(l//2):
  if s[i]!=s[l-1-i]:
    count+=1
print(count)
