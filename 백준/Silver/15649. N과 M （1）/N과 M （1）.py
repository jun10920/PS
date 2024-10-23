n, m = list(map(int, input().split()))

def back_tracking(arr, now_length, used_num):
  if now_length == m:
    print(*arr)
    return

  for i in range(1, n + 1):
    if not used_num[i]:
      arr.append(i)
      used_num[i] = True
      back_tracking(arr, now_length + 1, used_num)
      arr.pop()
      used_num[i] = False
      

nums = [i + 1 for i in range(n+1)]
used_num = [False] * (n + 1)
back_tracking([], 0, used_num)