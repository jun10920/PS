a, b = map(int, input().split())
temp=0
arr = [i for i in range(1, a+1)]
for _ in range(b):
  c, d = map(int, input().split())
  temp = arr[c-1: d]
  temp.reverse()
  arr[c-1: d] = temp

print(*(arr[i] for i in range(a)), end=" ")