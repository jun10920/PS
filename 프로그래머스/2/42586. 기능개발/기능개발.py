def solution(progress, speeds):
    # answer : 전체 답안을 더하는 배열
    # temp : 일시적으로 더하는 횟수를 저장하는 배열
    # progress 배열을 순회하면서, speeds의 배열을 순회하며 같은 인덱스에 더함
    #   progress의 맨 앞이 100이라면, 없애면서 temp에 +=1
    #   끝나면 answer append
    
    temp = 0
    answer = []
    
    while progress:
        for i in range(len(progress)):
            progress[i] += speeds[i]
            
        while progress and progress[0] >= 100:
            progress.pop(0)
            speeds.pop(0)
            temp += 1

        if temp > 0:
            answer.append(temp)
            temp = 0
    
    return answer