def solution(brown, yellow):
    # y는 카펫의 세로 길이, x는 카펫의 가로 길이
    for y in range(3, int((brown + yellow) ** 0.5) + 1):
        if (brown + yellow) % y == 0:  # 전체 카펫의 면적이 y로 나누어 떨어지는 경우
            x = (brown + yellow) // y
            if (x - 2) * (y - 2) == yellow:  # 노란색 격자 수 조건을 만족하는지 확인
                return [x, y]