s=input()
l=['01','02','03','04','05','06','07','08','09','10','11','12']
sforword=s[:2]
sback=s[2:]
if sforword in l:
  if sback in l:
    print('AMBIGUOUS')
  else:
    print('MMYY')
else:
  if sback in l:
    print('YYMM')
  else:
    print('NA')
