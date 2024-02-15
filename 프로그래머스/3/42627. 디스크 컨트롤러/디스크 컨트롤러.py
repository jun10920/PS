import heapq

def solution(jobs):
    jobs.sort()
    current_time, wait_list = 0, []
    job_index, total_time = 0, 0
    count = 0
    
    while count < len(jobs):
        while job_index < len(jobs) and jobs[job_index][0] <= current_time:
            heapq.heappush(wait_list, (jobs[job_index][1], jobs[job_index][0]))
            job_index += 1
        if wait_list:
            duration, start = heapq.heappop(wait_list)
            current_time += duration
            total_time += current_time - start
            count += 1
        else:
            current_time = jobs[job_index][0]
            
    return total_time // len(jobs)
    
    
    
    answer = 0
    return answer