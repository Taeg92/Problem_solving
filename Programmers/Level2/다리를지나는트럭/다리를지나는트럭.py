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

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

print(solution(bridge_length, weight, truck_weights))