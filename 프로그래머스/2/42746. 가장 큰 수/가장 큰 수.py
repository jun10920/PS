def solution(numbers):
    # 숫자를 문자열로 변환
    str_numbers = list(map(str, numbers))
    # 문자열 비교를 통해 정렬: 두 문자열 a, b에 대해 a+b와 b+a를 비교
    str_numbers.sort(key=lambda x: x*3, reverse=True)
    # 정렬된 문자열을 합침
    answer = ''.join(str_numbers)
    # 모든 숫자가 0일 경우를 처리
    return answer if answer[0] != '0' else '0'

# 예시 입력
numbers1 = [6, 10, 2]
numbers2 = [3, 30, 34, 5, 9]

# 함수 실행 및 결과 출력
print(solution(numbers1))  # "6210"
print(solution(numbers2))  # "9534330"
