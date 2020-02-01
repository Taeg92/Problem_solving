# Problem [1018] : 체스판 다시 칠하기

def find_chess(board, n, m):
    cnt_list = list()
    colors = ['B', 'W']
    for start_col in range(n-7):
        for start_row in range(m-7):
            for color_idx in range(len(colors)):
                cnt = 0
                for i in range(8):
                    for j in range(8):
                        if board[start_col+i][start_row+j] != colors[color_idx%2] :
                            cnt += 1
                        color_idx += 1
                    color_idx += 1
                cnt_list.append(cnt)
    return min(cnt_list)


n_val, m_val = map(int,input().split())
board = [list(input()) for _ in range(n_val)]
result = find_chess(board,n_val,m_val)
print(result)