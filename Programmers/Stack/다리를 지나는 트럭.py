# Problem : 다리를 지나는 트럭
from collections import deque

def solution(bridge_length, weight, truck_weights):
    bridge = deque([0]*bridge_length)
    after_pass = deque()
    trucks = deque(truck_weights)
    n_truck = len(trucks)
    t = 0
    while len(after_pass) != n_truck:
        if len(trucks) != 0:
            if bridge[0] != 0:
                after_pass.append(bridge.popleft())
                if sum(bridge) + trucks[0] <= weight: 
                    bridge.append(trucks.popleft())
                else:
                    bridge.append(0)
            else:
                bridge.popleft()
                if sum(bridge) + trucks[0] <= weight: 
                    bridge.append(trucks.popleft())
                else:
                    bridge.append(0)
        else:
            if bridge[0] != 0:
                after_pass.append(bridge.popleft())
                bridge.append(0)
            else:
                bridge.popleft()
                bridge.append(0)

        t += 1        
    answer = t
    return answer



bridge_length = 2
weight = 10
truck_weights = [7, 4, 5, 6]
answer = solution(bridge_length,weight,truck_weights)
print(answer)


bridge_length = 100
weight = 100
truck_weights = [10]
answer = solution(bridge_length,weight,truck_weights)
print(answer)


bridge_length = 100
weight = 100
truck_weights = [10, 10, 10, 10, 10, 10, 10, 10, 10, 10]
answer = solution(bridge_length,weight,truck_weights)
print(answer)