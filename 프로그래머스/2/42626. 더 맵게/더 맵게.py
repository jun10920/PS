import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # scoville 배열을 최소 힙으로 변환
    mix_count = 0  # 섞은 횟수

    while scoville[0] < K:  # 힙의 첫 번째 요소, 즉 가장 스코빌 지수가 낮은 음식이 K 이상이 될 때까지 반복
        if len(scoville) < 2:  # 더 이상 섞을 수 있는 음식이 없는 경우
            return -1  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없으므로 -1 반환
        
        least_spicy = heapq.heappop(scoville)  # 가장 스코빌 지수가 낮은 음식 제거
        second_least_spicy = heapq.heappop(scoville)  # 두 번째로 스코빌 지수가 낮은 음식 제거
        new_spicy = least_spicy + (second_least_spicy * 2)  # 두 음식을 섞어 새로운 음식 생성
        heapq.heappush(scoville, new_spicy)  # 새로운 음식을 힙에 추가
        mix_count += 1  # 섞은 횟수 증가

    return mix_count  # 모든 음식의 스코빌 지수가 K 이상이 되었을 때의 섞은 횟수 반환
