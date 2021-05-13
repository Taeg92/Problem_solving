def solution(s):
    num_list = list(map(int, s.split(' ')))
    return f'{str(min(num_list))} {str(max(num_list))}'


s = "-1 -2 -3 -4"

print(solution(s))
