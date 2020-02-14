
def solution(progresses, speeds):

    answer = []
    t = 0
    while 1:
        t += 1
        cnt = 0
        for i in range(len(progresses)):
            if progresses[i] != 0 and speeds[i] != 0:
                if progresses[i] + speeds[i]*t < 100:
                    break    
                else:    
                    cnt += 1
                    progresses[i] = 0
                    speeds[i] = 0
        if cnt > 0:
            answer.append(cnt)
        if sum(progresses) == 0:
            break
    return answer

progresses = [93, 30, 55]
speeds = [1, 30, 5]
print(solution(progresses,speeds))