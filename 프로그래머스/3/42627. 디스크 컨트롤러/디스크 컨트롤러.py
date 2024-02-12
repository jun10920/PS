import heapq

def solution(jobs):
    # 현재 시간과 대기 목록 초기화
    current_time, wait_list = 0, []
    # 요청 시간에 따라 jobs 정렬
    jobs.sort()
    # jobs 인덱스와 총 작업 시간 초기화
    job_index, total_time = 0, 0
    # 처리된 작업 수
    count = 0

    while count < len(jobs):
        # 현재 시간 이전에 요청된 모든 작업들을 대기 목록에 추가
        while job_index < len(jobs) and jobs[job_index][0] <= current_time:
            heapq.heappush(wait_list, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        
        if wait_list:
            # 대기 목록에서 처리 시간이 가장 짧은 작업을 선택
            duration, start = heapq.heappop(wait_list)
            # 현재 시간 업데이트
            current_time += duration
            # 총 작업 시간 업데이트 (현재 시간 - 요청 시간)
            total_time += current_time - start
            count += 1
        else:
            # 대기 목록이 비어있으면 현재 시간을 다음 작업의 요청 시간으로 업데이트
            current_time = jobs[job_index][0]

    # 모든 작업의 처리 완료 시간의 합계를 작업의 수로 나누어 평균을 구함
    return total_time // len(jobs)
