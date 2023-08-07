"""
정확성: 83.3
효율성: 16.7
합계: 100/100
"""
def solution(phone_book):
    book = {}

    for number in phone_book:
        book[number] = 1

    for number in phone_book:
        for idx in range(1, len(number)):
            if number[:idx] in book:
                return False

    return True

