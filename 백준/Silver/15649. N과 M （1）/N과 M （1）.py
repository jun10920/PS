n, m = list(map(int, input().split()))

import itertools

nums = [i for i in range(1, n + 1)]

arr = itertools.permutations(nums, m)

for i in arr:
  for j in i:
    print(j, end=' ')
  print()