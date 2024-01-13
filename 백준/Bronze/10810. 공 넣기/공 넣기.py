bin, ball = map(int, input().split())
arr = [0 for _ in range(bin)]
for _  in range(ball):
  i, j, k = map(int, input().split())
  arr[i-1:j] = [k] * (j-i+1)

for i in range(bin):
  print(arr[i], end=' ')