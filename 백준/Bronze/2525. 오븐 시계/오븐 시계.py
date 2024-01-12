h, m = map(int, input().split())
plusTime = int(input())
plusH = plusTime // 60
plusM = plusTime % 60

if m + plusM >= 60:
  h += plusH + 1
  m = (m + plusM) % 60
else:
  h += plusH
  m = (m + plusM)

print(h%24, m)