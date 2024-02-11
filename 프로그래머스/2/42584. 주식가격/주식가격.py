def solution(prices):
    length = len(prices)
    answer = [0] * length  # 가격이 떨어지지 않은 기간을 저장할 리스트 초기화
    stack = []  # 가격의 인덱스를 저장할 스택 초기화

    for i, price in enumerate(prices):
        # 스택이 비어있지 않고, 현재 가격이 스택의 맨 위 가격보다 낮은 경우
        while stack and price < prices[stack[-1]]:
            j = stack.pop()  # 스택에서 가격의 인덱스를 꺼냄
            answer[j] = i - j  # 가격이 떨어진 기간 계산
        stack.append(i)  # 현재 가격의 인덱스를 스택에 추가

    # 스택에 남은 가격들 처리
    while stack:
        j = stack.pop()
        answer[j] = length - 1 - j  # 남은 기간 계산

    return answer
