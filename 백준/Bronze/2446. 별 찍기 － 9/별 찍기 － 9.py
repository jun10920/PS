num = int(input())

for i in range(2*num,1,-1):
  if i % 2 == 0:
    continue
  else:
    print(int((2*num-1-i)/2)*" "+i*"*")


for i in range(1, 2*num):
  if i % 2 == 0:
    continue
  else:
    print(int((2*num-1-i)/2)*" "+i*"*")