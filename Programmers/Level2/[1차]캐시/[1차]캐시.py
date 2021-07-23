from collections import deque


def solution(cacheSize, cities):
    answer = 0
    buffer = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()
        if city in buffer:
            answer += 1
            buffer.remove(city)
        else:
            answer += 5
            if len(buffer) >= cacheSize:
                buffer.popleft()

        buffer.append(city)
    return answer


cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork",
          "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]

print(solution(cacheSize, cities))
