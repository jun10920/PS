from collections import deque

def solution(priorities, location):
    # (우선순위, 초기 위치) 형태로 큐에 프로세스 정보를 저장
    queue = deque([(priority, i) for i, priority in enumerate(priorities)])
    answer = 0  # 실행 순서를 카운트할 변수

    while queue:
        current = queue.popleft()  # 현재 프로세스를 큐에서 꺼냄
        # any 함수를 사용하여 현재 프로세스보다 우선순위가 높은 프로세스가 큐에 있는지 검사
        if any(current[0] < other[0] for other in queue):
            queue.append(current)  # 우선순위가 더 높은 프로세스가 있다면 큐의 끝에 다시 추가
        else:
            answer += 1  # 현재 프로세스를 실행하므로 카운터 증가
            if current[1] == location:  # 현재 프로세스가 찾고 있는 프로세스라면
                return answer  # 현재까지의 실행 순서를 반환

    return answer
