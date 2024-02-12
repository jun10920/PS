def solution(array, commands):
    answer = []
    for i in commands:
        left = i[0] - 1
        right = i[1]
        index = i[2] - 1
        arr = array[left:right]
        arr.sort()
        answer.append(arr[index])
    return answer
