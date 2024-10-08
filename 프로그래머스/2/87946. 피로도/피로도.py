def dfs(current_hp, visited, dungeons, count):
    
    global answer
    answer = max(answer, count)
    
    for i in range(len(dungeons)):
        min_hp, use_hp = dungeons[i]
        if not visited[i] and  current_hp >= min_hp:
            visited[i] = True
            dfs(current_hp - use_hp, visited, dungeons, count + 1)
            visited[i] = False
        

def solution(k, dungeons):
    global answer
    answer = -1
    
    visited = [False] * len(dungeons)
    
    dfs(k, visited, dungeons, 0)
    
    return answer