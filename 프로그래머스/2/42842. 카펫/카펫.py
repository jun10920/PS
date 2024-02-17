def solution(brown, yellow):
    for i in range(3, int(brown + yellow**(0.5)) + 1):
        if (brown + yellow) % i == 0:
            y = (brown + yellow) // i
            x = (brown + yellow) // y
            if (x-2)*(y-2) == yellow and x >= y:
                return [x,y]
    
            