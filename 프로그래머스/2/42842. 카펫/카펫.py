def solution(brown, yellow):
    
    total = brown + yellow
    answer = []
    
    for height in range(1, int(total**0.5) + 1):
        
        if total % height == 0:
            width = total // height
            
            if (width - 2) * (height - 2) == yellow:
                return [width, height]