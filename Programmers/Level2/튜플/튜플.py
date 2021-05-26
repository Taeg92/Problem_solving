def solution(s):
    answer = []
    s = s[2:-2]
    s = s.split("},{")
    s.sort(key=lambda x: len(x))
    for num_str in s:
        num_list = num_str.split(",")
        for num in num_list:
            if int(num) not in answer:
                answer.append(int(num))
    return answer


s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))
