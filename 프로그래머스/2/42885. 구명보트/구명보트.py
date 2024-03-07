def solution(people, limit):
    people.sort()  # 사람들의 몸무게를 오름차순으로 정렬
    left, right = 0, len(people) - 1  # 투 포인터 초기화
    count = 0

    while left <= right:
        if people[left] + people[right] <= limit:
            left += 1  # 가장 가벼운 사람을 다음 사람으로 업데이트
        right -= 1  # 가장 무거운 사람을 이전 사람으로 업데이트
        count += 1  # 보트 수 증가

    return count
