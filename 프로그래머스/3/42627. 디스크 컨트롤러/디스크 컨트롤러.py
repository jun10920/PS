import heapq

def solution(jobs):
    jobs.sort()
    job_idx = 0
    current_time = 0
    wait_list = []
    total_time = 0
    count = 0
    
    while count < len(jobs):
        while job_idx < len(jobs) and jobs[job_idx][0] <= current_time:
            heapq.heappush(wait_list, (jobs[job_idx][1], jobs[job_idx][0]))
            job_idx += 1
        
        if wait_list:
            duration, start = heapq.heappop(wait_list)
            current_time += duration
            total_time += current_time - start
            count += 1
        else:
            current_time = jobs[job_idx][0]
    return total_time // len(jobs)