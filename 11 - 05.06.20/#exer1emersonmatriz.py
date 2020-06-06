m=[[0 for i in range(4)]for i in range(3)]
res=0
for l in range(3):
  for c in range(4):
    m[l][c]=int(input())
for i in range(3):
  res=res+m[2][i]
print(res)