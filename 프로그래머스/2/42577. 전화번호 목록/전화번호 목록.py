def solution(phone_book):
    phone_book.sort()  # 전화번호 목록을 사전순으로 정렬
    for i in range(len(phone_book) - 1):
        if phone_book[i+1].startswith(phone_book[i]):  # 다음 번호가 현재 번호로 시작하는지 확인
            return False
    return True
