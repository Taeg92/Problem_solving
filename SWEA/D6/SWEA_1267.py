# Problem [1267] : 작업순서

T = 10
for tc in range(1,T+1):
    V, E = map(int,input().split())
    data = list(map(int,input().split()))
    graph = [[0]*(V+1) for _ in range(V+1)]
    result = list()
    queue = list()

    N = len(data)//2
    for i in range(N):
        graph[data[i*2+1]][data[i*2]] = 1

    for i in range(1, V+1):
        if 1 not in graph[i]:
            queue.append(i)

    while 1:
        if len(result) == V:
            break
        else:
            q = queue.pop(0)
            result.append(q)
            for i in range(1,V+1):
                if graph[i][q] == 1:
                    graph[i][q] = 0
                    if 1 not in graph[i]:
                        queue.append(i)
    print('#{} {}'.format(tc,' '.join(map(str,result))))