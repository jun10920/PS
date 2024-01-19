m, d = map(int, input().split())


sum = 0

for i in range(1, m):
  if i in [1,3,5,7,8,10,12]:
    sum += 31
  elif i in [4,6,9,11]:
    sum += 30
  elif i == 2:
    sum += 28

# 현재 월의 일자를 더함
sum += d - 1  # 1월 1일을 월요일로 기준으로 하므로, 1을 빼줍니다.

# 요일 계산
sum %= 7

# 결과 출력
if sum == 0:
    print("MON")
elif sum == 1:
    print("TUE")
elif sum == 2:
    print("WED")
elif sum == 3:
    print("THU")
elif sum == 4:
    print("FRI")
elif sum == 5:
    print("SAT")
elif sum == 6:
    print("SUN")