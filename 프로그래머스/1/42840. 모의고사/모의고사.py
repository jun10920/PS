def solution(answers):
    num1, num2, num3 = 0, 0, 0
    
    answer1 = [1,2,3,4,5]
    answer2 = [2,1,2,3,2,4,2,5]
    answer3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i, v in enumerate(answers):
        if answer1[i % 5] == answers[i]:
            num1 += 1
        if answer2[i % 8] == answers[i]:
            num2 += 1
        if answer3[i % 10] == answers[i]:
            num3 += 1
    
    temp = []
    temp+=[num1, num2, num3]
    
    print(temp)
    
    answer = []
    
    top = max(temp)
    for i, v in enumerate(temp):
        if v == top:
            answer.append(i+1)
    
    return answer