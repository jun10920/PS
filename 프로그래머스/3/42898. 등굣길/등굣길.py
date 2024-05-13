def solution(m, n, puddles):
    # 맵 초기화 (1-based index 사용을 위해 m+1, n+1 크기로 생성)
    map = [[0] * (m + 1) for _ in range(n + 1)]
    
    # 웅덩이 표시
    for p in puddles:
        map[p[1]][p[0]] = -1
    
    # 시작점 초기화
    if map[1][1] == -1:
        return 0
    else:
        map[1][1] = 1
    
    # 경로 수 계산
    for y in range(1, n + 1):
        for x in range(1, m + 1):
            if map[y][x] == -1 or (x == 1 and y == 1): # 웅덩이이거나 시작점인 경우
                continue
            # 왼쪽 또는 위쪽에서 오는 경로가 유효한 경우 해당 값을 현재 위치에 추가
            if map[y][x-1] > 0:
                map[y][x] += map[y][x-1]
            if map[y-1][x] > 0:
                map[y][x] += map[y-1][x]

    # 마지막 지점 반환
    return map[n][m] % 1000000007
