def solution(s):
    # 빈 문자열인 경우 올바른 괄호 문자열로 간주
    if not s:
        return True

    # 문자열의 첫 문자가 ')'이거나 마지막 문자가 '('인 경우 바로 False 반환
    if s[0] == ')' or s[-1] == '(':
        return False
    
    counter = 0  # 괄호의 균형을 확인하기 위한 카운터

    for char in s:
        if char == '(':  # 여는 괄호를 만나면 카운터 증가
            counter += 1
        else:  # 닫는 괄호를 만나면 카운터 감소
            counter -= 1
            if counter < 0:  # 카운터가 음수가 되면 올바르지 않은 괄호
                return False

    # 모든 괄호를 검사한 뒤 카운터가 0이 아니면 올바르지 않은 괄호
    return counter == 0
