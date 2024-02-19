def solution(name):
    
    result = 0
    for i in name:
        result += min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
    LR = len(name) - 1
    for i in range(len(name)):
        temp = 0
        if name[i] == 'A':
            temp = i
            while temp < len(name) and name[temp] == 'A':
                temp += 1
            left = 0 if i == 0 else i - 1
            right = len(name) - temp
            LR = min(LR, left + right + min(left, right))
    result = LR + result

    return result