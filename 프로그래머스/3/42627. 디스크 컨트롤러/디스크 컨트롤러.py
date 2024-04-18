import heapq

def solution(jobs):
    # 요청 시간에 따라 jobs 정렬
    jobs.sort(reverse=True)
    # 우선순위 큐 초기화
    pq = []
    # 현재 시간, 총 대기 시간, 처리한 작업 수
    current_time, total_wait_time, count = 0, 0, 0
    # 전체 작업 수
    total_jobs = len(jobs)

    while count < total_jobs:
        # 현재 시간 이전에 요청된 모든 작업을 우선순위 큐에 추가
        while jobs and jobs[-1][0] <= current_time:
            job = jobs.pop()
            heapq.heappush(pq, (job[1], job[0]))  # 수행 시간을 기준으로 힙에 추가
        
        if pq:
            # 우선순위 큐에서 가장 짧은 작업을 꺼내어 처리
            duration, start_time = heapq.heappop(pq)
            current_time += duration
            total_wait_time += current_time - start_time
            count += 1
        else:
            # 대기 중인 작업이 없다면, 다음 작업의 요청 시간으로 시간을 옮김
            current_time = jobs[-1][0]

    return total_wait_time // total_jobs
