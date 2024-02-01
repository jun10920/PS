def solution(n, lost, reserve):
    
    totalPeopleNum = n
    
    lostArr = [i for i in lost if i not in reserve]
    reserveArr = [i for i in reserve if i not in lost]
    
    lostArr.sort()
    reserveArr.sort()
    
    for i in reserveArr:
        if i-1 in lostArr:
            lostArr.remove(i-1)
        elif i+1 in lostArr:
            lostArr.remove(i+1)
    print(lostArr)

    return n-len(lostArr)