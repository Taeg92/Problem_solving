def solution(citations):
    for h in range(max(citations), 0, -1):
        up_cnt = 0
        for num in citations:
            if num >= h:
                up_cnt += 1
            if up_cnt == h:
                return h
    return 0

citations = [3, 0, 6, 1, 5];
print(solution(citations))