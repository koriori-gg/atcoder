n=[int(i) for i in input()]
for i in range(3):
  if n[i]==n[i+1]:
    print('Bad')
    exit()
else:
  print('Good')
