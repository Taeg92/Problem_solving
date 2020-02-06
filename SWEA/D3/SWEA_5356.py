# Problem [5356] : 의석이의 세로로 말해요


T = int(input())

for tc in range(1, T+1):
    
    data = [list(input()) for _ in range(5)]
    row_data = [data[j][i] for i in range(15) for j in range(5) if i < len(data[j])]
    print('#{} {}'.format(tc, ''.join(row_data)))
