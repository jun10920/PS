import sys

input = sys.stdin.readline

channel = int(input())

brokenBtns = int(input())

brokenBtn = list(input().split())
num = abs(100 - channel)

for i in range(1000001):
  for j in str(i):
    if j in brokenBtn:
      break
  else:
    num = min(num, len(str(i)) + abs(i - channel))

print(num)
