def solution(answers):
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    
    scores = [0,0,0]
    
    for i, v in enumerate(answers):
        if v == arr1[i%5]:
            scores[0] += 1
        if v == arr2[i%8]:
            scores[1] += 1
        if v == arr3[i%10]:
            scores[2] += 1
    
    highest = max(scores)

    return [i+1 for i,v in enumerate(scores) if v == highest]