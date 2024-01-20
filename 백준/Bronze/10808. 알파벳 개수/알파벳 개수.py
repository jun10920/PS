import sys
input = sys.stdin.readline().rstrip

alphaArr = [chr(ord('a') + i) for i in range(26)]

resultArr = [0 for i in range(26)]

sen = input()

for i in sen:
  if i in alphaArr:
    resultArr[alphaArr.index(i)] += 1

print(" ".join(map(str, resultArr)))
    