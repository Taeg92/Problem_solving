import heapq

def solution(scoville, K):
    heapq.heapify(scoville)
    answer = 0
    while len(scoville) >= 2:
        if scoville[0] >= K:
            return answer
        heapq.heappush(scoville, heapq.heappop(scoville) + (heapq.heappop(scoville) * 2))
        if scoville[0] >= K:
            return answer+1
        answer += 1

    return -1

scoville = [1, 2, 3, 9, 10, 12]
K = 7
print(solution(scoville, K))