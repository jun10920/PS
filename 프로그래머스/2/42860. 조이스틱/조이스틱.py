def solution(name):
    answer = 0
    # 상하 조작횟수 구하기
    for i in name:
        answer += min(ord(i)-ord('A'), ord('Z')-ord(i)+1)
        
    print(answer)
    # 좌우 조작횟수 구하기
    sum = len(name) -1
    for i in range(len(name)):
        temp = 0
        if name[i] == 'A':
            temp = i
            while temp < len(name) and name[temp] == 'A':
                temp += 1
            left=(0 if i==0 else i-1)
            right = len(name) - temp
            sum = min(sum, left + right + min(left, right))
    answer += sum
    print(answer)
    return answer