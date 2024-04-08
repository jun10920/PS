def solution(phone_book):
    phone_hash = {phone: True for phone in phone_book}
    
    for phone in phone_book:
        prefix = ""
        for number in phone:
            prefix += number
            if prefix in phone_hash and prefix != phone:
                return False
                
    return True
