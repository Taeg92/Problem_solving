def solution(phone_number):
    answer = ''
    numbers = phone_number[-4:]
    answer = '*'*(len(phone_number)-4) + numbers
    return answer

phone_number = "01033334444"
print(solution(phone_number))