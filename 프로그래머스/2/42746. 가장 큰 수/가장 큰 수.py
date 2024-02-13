def solution(numbers):
    strN = list(map(str,numbers))
    strN.sort(key=lambda x: x*3, reverse = True)
    answer = ''.join(strN)
    return answer if answer[0] != '0' else '0'