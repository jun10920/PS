def solution(answers):
    man1 = [1, 2, 3, 4, 5]
    man2 = [2, 1, 2, 3, 2, 4, 2, 5]
    man3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == man1[i%5]:
            score[0] += 1
        if answers[i] == man2[i%8]:
            score[1] += 1
        if answers[i] == man3[i%10]:
            score[2] += 1
    
    maxAn = max(score)
    
    return [i + 1 for i, v in enumerate(score) if v == maxAn]