from itertools import product
def solution(word):
    arr = ['A', 'E', 'I', 'O', 'U']
    answerArr = []
    for i in range(1, len(arr) + 1):
        answerArr += list(product(arr, repeat = i))
    
    answerArr = list(map(lambda x : ''.join(x), answerArr))
    answerArr.sort()
    answer = answerArr.index(word) + 1
    return answer