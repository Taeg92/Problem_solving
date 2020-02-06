# Problem[4615] : 재미있는 오셀로 게임

T = int(input())

for tc in range(1, T+1):

    N, M = map(int, input().split())
    data = list([0]*N for _ in range(N))
    B_cnt = 0
    W_cnt = 0
    center = N//2
    data[center][center] = 2
    data[center-1][center] = 1
    data[center][center-1] = 1
    data[center-1][center-1] = 2
 
    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    for _ in range(M):
        x, y, stone = map(int, input().split())
        x -= 1
        y -= 1
        data[x][y] = stone
        for i in range(8):
            x_axis = x + dx[i]
            y_axis = y + dy[i]
            temp = list()
            while 0 <= x_axis < N and 0 <= y_axis < N:
                if data[x_axis][y_axis] == 0:
                    break
                elif data[x_axis][y_axis] != stone:
                    temp.append(x_axis)
                    temp.append(y_axis)
                elif data[x_axis][y_axis] == stone:
                    while temp:
                        c_y = temp.pop()
                        c_x = temp.pop()
                        data[c_x][c_y] = stone
                    break
                x_axis += dx[i]
                y_axis += dy[i]
    for i in range(N):
        B_cnt += data[i].count(1)
        W_cnt += data[i].count(2)
    print('#{} {} {}'.format(tc, B_cnt, W_cnt))