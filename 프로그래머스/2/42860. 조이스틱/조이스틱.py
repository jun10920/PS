def solution(name):
    
    result = 0
    
    for i in name:
        result += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
    
    LR = len(name) - 1
    startIdx = 0
    temp = 0
    for i in range(len(name)):
        if name[i] == 'A':
            startIdx = i
            temp = i
            print(temp)
            while temp < len(name) and name[temp] == 'A':
                temp += 1
            left = 0 if i==0 else startIdx-1
            right = len(name) - temp
            LR = min(LR, left+right+min(left, right))
    return result + LR