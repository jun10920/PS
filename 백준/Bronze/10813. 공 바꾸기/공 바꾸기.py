bin, ball = map(int, input().split())
arr = [0]*bin
for i  in range(bin):
  arr[i] = i+1

for _ in range(ball): 
  a, b = map(int, input().split())
  temp = arr[a-1]
  arr[a-1] = arr[b-1]
  arr[b-1] = temp

for i in range(bin):
  print(arr[i], end=" ")