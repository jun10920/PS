def solution(people, limit):
    people.sort(reverse = True)
    light_idx = len(people) - 1
    heavy_idx = 0
    boats = 0
    
    while heavy_idx <= light_idx:
        
        if people[light_idx] + people[heavy_idx] <= limit:
            light_idx -=1
        
        boats += 1
        heavy_idx += 1
    
    return boats