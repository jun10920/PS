from collections import deque

def bfs(begin, target, words):
    
    queue = deque([(begin, 0)])
    
    while queue:
        begin, count = queue.popleft()
        
        if begin == target:
            return count
        
        for word in words[:]:
            if wordDiffByOne(begin, word):
                queue.append((word, count +1))
                words.remove(word)
                
def wordDiffByOne(word1, word2):
    return 1 == sum(1 for a, b in zip(word1, word2) if a !=b)

def solution(begin, target, words):
    
    if target not in words:
        return 0
    else:
        return bfs(begin, target, words)