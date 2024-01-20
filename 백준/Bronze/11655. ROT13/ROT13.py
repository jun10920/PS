import sys
input = sys.stdin.readline().rstrip

smallAlphaArr = [chr(ord('a') + i) for i in range(26)]
bigAlphaArr = [chr(ord('A') + i) for i in range(26)]

sen = input()

for i in sen:
  if i in smallAlphaArr:
    if ord(i) + 13 > ord('z'):
      print(chr(ord(i) - 13), end='')
    else:
      print(smallAlphaArr[smallAlphaArr.index(i)+13], end='')
  elif i in bigAlphaArr:
    if ord(i) + 13 > ord('Z'):
      print(chr(ord(i) - 13), end='')
    else:
      print(bigAlphaArr[bigAlphaArr.index(i)+13], end='')
  else:
    print(i, end='')