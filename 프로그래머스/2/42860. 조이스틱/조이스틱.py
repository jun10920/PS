def solution(name):
    answer = 0
    for i in name:
        answer += min(ord(i)-ord('A'), ord('Z')-ord(i)+1)

    tmp=0
    shift=len(name)-1
    for i in range(len(name)):
        if name[i]=="A":
            tmp=i
            while(tmp<len(name) and name[tmp]=="A"):
                tmp+=1
            left=(0 if i==0 else i-1)
            right=len(name)-tmp
            shift=min(shift,left+right+min(left,right))
    answer+=shift
    return answer