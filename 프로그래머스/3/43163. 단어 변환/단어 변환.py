from collections import deque

def bfs(begin, target, words):
    queue = deque([(begin, 0)])
    
    while queue:
        current_word, count = queue.popleft()
        
        if current_word == target:
            return count
        
        for word in words[:]:
            if diff_by_one(current_word, word):
                queue.append((word, count + 1))

def diff_by_one(word1, word2):
    cnt = sum(1 for a, b in zip(word1, word2) if a != b)
    return cnt == 1

def solution(begin, target, words):
    if target not in words:
        return 0
    else:
        return bfs(begin, target, words)