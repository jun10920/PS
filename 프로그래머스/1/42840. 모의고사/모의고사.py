from itertools import cycle

arr = [
    cycle([1,2,3,4,5]),
    cycle([2,1,2,3,2,4,2,5]),
    cycle([3,3,1,1,2,2,4,4,5,5])
]
score = [0,0,0]

def solution(answers):
    for i in answers:
        for j in range(3):
            if i == next(arr[j]):
                score[j] += 1

    highest = max(score)
    result = []
    for i in range(len(score)):
        if score[i] == highest:
            result.append(i+1)
    return result