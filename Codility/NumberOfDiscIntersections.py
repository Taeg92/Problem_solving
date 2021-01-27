def solution(A):
    # write your code in Python 3.6
    boundarys = []

    for idx, radius in enumerate(A):
        boundarys.append((idx - radius, -1))
        boundarys.append((idx + radius, 1))

    boundarys.sort()

    intersections = 0
    intervals = 0

    for boundary in boundarys:
        if boundary[1] == 1:
            intervals -= 1
        if boundary[1] == -1:
            intersections += intervals
            intervals += 1

    return -1 if intersections > 10000000 else intersections


A = [1, 5, 2, 1, 4, 0]

print(solution(A))
