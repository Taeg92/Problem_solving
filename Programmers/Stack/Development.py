
def solution(progresses, speeds):

    answer = []
    t = 0
    while progresses:
        t += 1
        i = 0
        for _ in range(len(progresses)):
            if progresses[i] - speeds[i]*t <= 0:
                progresses.pop(i)
                speeds.pop(i)
                i -= 1
            else :
                i += 1
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses,speeds))