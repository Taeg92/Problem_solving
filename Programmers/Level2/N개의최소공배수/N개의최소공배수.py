def lcs(a, b):
    if a % b == 0: 
        return b 
    else:
        return lcs(b, (a % b))

def solution(arr):
    answer = 1 
    for num in arr:
        answer = (answer * num) // lcs(answer, num)
    return answer

arr = [2,6,8,14]
print(solution(arr))