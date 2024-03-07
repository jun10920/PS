from collections import deque

def bfs(begin, target, words):
    queue = deque([(begin, 0)])
    
    while queue:
        current_word, count = queue.popleft()
        
        if current_word == target:
            return count
        
        for word in words[:]:
            if word_diff_by_one(current_word, word):
                queue.append((word, count + 1))
                words.remove(word)
    return 0

def word_diff_by_one(word1, word2):
    diff_count = sum(1 for a, b in zip(word1, word2) if a != b)
    return diff_count == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    return bfs(begin, target, words)