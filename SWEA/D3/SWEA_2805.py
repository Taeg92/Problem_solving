# Problem [2805] : 농작물 수확하기

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int,input())) for _ in range(N)]
    s = 0
    for i in range(N//2+1): 
        for j in range(N//2-i,i+N//2+1): 
            s += data[i][j]
    for i in range(N-1, N//2, -1):  
        for j in range(i-N//2, N//2+N-i):
            s += data[i][j]
    
    print('#{} {}'.format(tc,s))