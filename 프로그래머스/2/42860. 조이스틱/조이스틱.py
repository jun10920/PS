def solution(name):
    result = 0
    min_move = len(name) - 1  # 최소 이동 횟수 초기값 설정: 오른쪽으로만 이동하는 경우

    for i, char in enumerate(name):
        # 각 문자를 원하는 알파벳으로 변경하기 위한 조작 횟수 계산
        result += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        # 다음 문자부터 연속된 A의 마지막 인덱스 찾기
        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        # 현재 위치에서 오른쪽 또는 왼쪽으로 이동하는 경우 중 최소 이동 횟수 계산
        # min_move = min(현재까지의 이동 횟수 + (전체 길이 - 연속된 A 이후의 인덱스), 기존의 최소 이동 횟수)
        # i*2는 현재 위치로 돌아오기 위한 이동 횟수를 뜻함
        min_move = min(min_move, i + len(name) - next + min(i, len(name) - next))

    result += min_move  # 알파벳 변경을 위한 조작 횟수와 커서 이동을 위한 조작 횟수를 더함
    return result
