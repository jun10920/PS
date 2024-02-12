def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        day = -((progress - 100)// speed)
        days.append(day)
    days.reverse()
    answer = []
    while days:
        current_day = days.pop()
        count = 1
        while days and days[-1] <= current_day:
            days.pop()
            count += 1
        answer.append(count)     
    return answer