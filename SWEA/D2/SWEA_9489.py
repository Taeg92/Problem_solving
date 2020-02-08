# Problem [9489] : 고대 유적

T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    col_data = [''.join(input().split()) for _ in range(N)]
    row_data = [''.join(map(str,i)) for i in zip(*col_data)]
    m = 0
    col = list()
    row = list()
    for data in col_data:
        col.append(data.split('0'))
    for data in row_data:
        row.append(data.split('0'))
    
    for data in col:
        for structure in data:
            if len(structure) > m:
                m = len(structure)
    for data in row:
        for structure in data:
            if len(structure) > m:
                m = len(structure)
    print('#{} {}'.format(tc,m))    