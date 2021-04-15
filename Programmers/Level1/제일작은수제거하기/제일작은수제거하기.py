def solution(arr):
    answer = []
    arr.remove(min(arr))
    answer = arr
    if not answer:
        answer.append(-1)
    return answer

arr = [4, 3, 2, 1]
print(solution(arr))