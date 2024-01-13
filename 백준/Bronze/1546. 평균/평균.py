num = int(input())
sum = 0

arr = list(map(int, input().split()))
maxArr = max(arr)

for i in range(num):
  arr[i] = arr[i]/maxArr*100
  sum += arr[i]

print(sum/num)