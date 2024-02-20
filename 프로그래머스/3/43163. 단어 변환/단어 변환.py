from collections import deque

def bfs(words, target, begin):
    queue = deque([(begin, 0)])  # 시작 단어와 단계를 함께 큐에 추가
    
    while queue:
        current_word, count = queue.popleft()  # 현재 단어와 현재 단계를 함께 꺼냄
        
        if current_word == target:
            return count  # 목표 단어에 도달했을 경우 현재 단계 반환
        
        for word in words[:]:  # words의 복사본을 순회하여 원본 리스트 수정 시 문제 방지
            if word_diff_by_one(current_word, word):
                queue.append((word, count + 1))  # 다음 단어와 다음 단계를 큐에 추가
                words.remove(word)  # 사용한 단어는 리스트에서 제거하여 중복 방지
    return 0  # 변환할 수 없는 경우 0 반환

def word_diff_by_one(word1, word2):
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1  # 두 단어 간 차이가 한 글자인지 확인

def solution(begin, target, words):
    if target not in words:
        return 0  # 변환할 수 없는 경우 0 반환
    return bfs(words, target, begin)  # BFS 실행하여 결과 반환
