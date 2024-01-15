num = int(input())

for _ in range(num):
  a, b = input().split()
  for j in range(len(b)):
    print(b[j]*int(a), end='')
  print()