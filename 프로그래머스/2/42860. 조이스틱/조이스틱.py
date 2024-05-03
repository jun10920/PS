def solution(name):
    answer = 0
    # 각 문자를 조작하여 목표 알파벳으로 만드는데 필요한 최소 조작 횟수를 더합니다.
    for char in name:
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

    # 커서 이동 최소화를 위한 계산
    min_move = len(name) - 1  # 오른쪽으로만 이동하는 경우
    for idx in range(len(name)):
        next_idx = idx + 1
        # 연속된 'A' 문자열이 얼마나 긴지 확인하고 건너뛰기
        while next_idx < len(name) and name[next_idx] == 'A':
            next_idx += 1
        
        # 왼쪽으로 돌아가는 경우와 오른쪽으로 계속 가는 경우 중 최소 이동 거리 계산
        distance = min(idx, len(name) - next_idx)
        min_move = min(min_move, idx + len(name) - next_idx + distance)

    answer += min_move
    return answer
