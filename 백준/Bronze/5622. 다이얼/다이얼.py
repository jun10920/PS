dial = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
sum = 0
a = input()

for i in range(len(a)):
  for j in dial:
    if a[i] in j:
      sum = sum + dial.index(j)+3
print(sum)