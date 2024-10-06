from collections import Counter
def solution(clothes):
    
    temp = []
    
    for i in clothes:
        temp.append(i[1])
        
    counter = Counter(temp)
    
    print(counter.values())
    
    answer = 1
    for i in counter.values():
        answer *= (i + 1)
    
    return answer - 1