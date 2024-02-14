from itertools import product

def solution(word):
    characters = ['A', 'E', 'I', 'O', 'U']
    arr = []

    # 1글자에서 5글자까지 가능한 모든 조합을 생성하여 arr에 추가
    for i in range(1, 6):
        for combination in product(characters, repeat=i):
            arr.append(''.join(combination))

    arr.sort()  # 생성된 문자열을 사전 순으로 정렬
    answer = arr.index(word) + 1  # 주어진 word의 인덱스를 찾고, 문제의 조건에 맞게 1을 더함
    return answer
