s=str(input())
l=len(s)
count=0
if l==1:
  if 'L' in s:
    ans='No'
  else:
    ans='Yes'
if 'L' in s[::2] or 'R' in s[1::2]:
  ans='No'
else:
  ans='Yes'
print(ans)
