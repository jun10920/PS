def solution(arr):
    # 결과를 저장할 리스트 초기화
    result = [arr[0]]

    # 배열 arr의 두 번째 원소부터 확인
    for num in arr[1:]:
        # 현재 숫자가 결과 리스트의 마지막 원소와 다르면 추가
        if num != result[-1]:
            result.append(num)

    # 수정된 결과 반환
    return result
