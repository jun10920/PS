from collections import deque

def word_diff_by_one(word1, word2):
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    
    queue = deque([(begin, 0)])  # (현재 단어, 변환 횟수)
    while queue:
        current_word, step_count = queue.popleft()
        
        if current_word == target:
            return step_count
        
        for word in words[:]:
            if word_diff_by_one(current_word, word):
                queue.append((word, step_count + 1))
                words.remove(word)  # 방문한 단어 제거
                
    return 0
