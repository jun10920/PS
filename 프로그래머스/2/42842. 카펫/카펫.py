def solution(brown, yellow):
    for i in range(3, int((brown + yellow)**(1/2)) + 1):
        if (brown + yellow) % i == 0:
            y = i
            x = (brown + yellow) // y
            if (x - 2) * (y - 2) == yellow:
                return [x, y]