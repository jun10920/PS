import heapq

def solution(jobs):
    jobs.sort()  # 요청 시간 기준으로 정렬 (jobs[i][0]이 요청 시간)
    
    total_time = 0
    current_time = 0
    idx = 0  # jobs 리스트에서 탐색할 인덱스
    heap = []  # 대기 중인 작업을 넣을 최소 힙
    count = 0  # 완료된 작업 수
    
    while count < len(jobs):
        # 현재 시점에 요청된 작업을 모두 heap에 넣는다.
        while idx < len(jobs) and jobs[idx][0] <= current_time:
            heapq.heappush(heap, (jobs[idx][1], jobs[idx][0]))  # (작업 소요 시간, 요청 시간) 순으로 힙에 삽입
            idx += 1
        
        if heap:
            # 대기 중인 작업 중에서 소요 시간이 가장 적은 작업 처리
            job_time, job_start = heapq.heappop(heap)
            current_time += job_time  # 현재 시간 업데이트
            total_time += (current_time - job_start)  # 총 대기 시간 계산
            count += 1
        else:
            # 대기 중인 작업이 없으면 시간을 요청 시간으로 맞춘다.
            current_time = jobs[idx][0]
    
    return total_time // len(jobs)
