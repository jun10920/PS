import sys

input = sys.stdin.readline().rstrip

sen = input()

arr = [sen[i:len(sen)] for i in range(len(sen))]
arr.sort()
for i in arr:
  print(i)