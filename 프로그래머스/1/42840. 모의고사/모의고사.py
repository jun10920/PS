def solution(answer):
    arr1 = [1,2,3,4,5]
    arr2 = [2,1,2,3,2,4,2,5]
    arr3 = [3,3,1,1,2,2,4,4,5,5]
    
    score = [0,0,0]
    
    for i in range(len(answer)):
        if answer[i] == arr1[i%5]:
            score[0] +=1
        if answer[i] == arr2[i%8]:
            score[1] +=1
        if answer[i] == arr3[i%10]:
            score[2] +=1
    highest = max(score)
    
    result = [i +1  for i, v in enumerate(score) if v == highest]   
   
    return result