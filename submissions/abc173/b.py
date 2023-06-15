n=int(input())
count_ac=0
count_wa=0
count_tle=0
count_re=0
for i in range(n):
  s=input()
  if s=='AC':
    count_ac+=1
  elif s=='WA':
    count_wa+=1
  elif s=='TLE':
    count_tle+=1
  else:
    count_re+=1
print('AC x',count_ac)
print('WA x',count_wa)
print('TLE x',count_tle)
print('RE x',count_re)
