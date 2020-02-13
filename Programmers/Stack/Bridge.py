# Problem : 다리를 지나는 트럭

from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    trucks = deque(truck_weights)
    t = 0
    if sum(trucks) == 0:
        return 0
    while bridge:
        t += 1
        bridge.popleft()
        if trucks:
            if sum(bridge)+trucks[0]<=weight:
                bridge.append(trucks.popleft())
            else:
                bridge.append(0)
    
    answer = t
    return answer



bridge_length = 5
weight = 5
truck_weights = [2, 2, 2, 2, 1, 1, 1, 1, 1]
answer = solution(bridge_length,weight,truck_weights)
print(answer)