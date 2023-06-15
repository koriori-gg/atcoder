s=input()
count=0
s=list(s)
kisu=s[0::2]
gusu=s[1::2]
komoji = ''.join(kisu)
omoji = ''.join(gusu)
if len(s)>=2:
  if ((komoji.islower())==True) and ((omoji.isupper())==True):
    print('Yes')
  else:
    print('No')
else:
  if (komoji.islower())==True:
    print('Yes')
  else:
    print('No')
  
