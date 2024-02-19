def solution(numbers, target):
    def dfs(index, current):
        # 종료 조건: 모든 숫자를 확인했을 때
        if index == len(numbers):
            # 현재 값이 타겟 넘버와 같으면 1 반환, 그렇지 않으면 0 반환
            return 1 if current == target else 0
        else:
            # 현재 숫자를 더하는 경우와 빼는 경우로 나누어 재귀 호출
            return dfs(index + 1, current + numbers[index]) + dfs(index + 1, current - numbers[index])

    # 초기 인덱스는 0, 초기 값은 0으로 설정하고 DFS 시작
    return dfs(0, 0)
