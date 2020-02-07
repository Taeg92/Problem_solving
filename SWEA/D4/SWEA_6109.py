# Problem [6109] : 추억의 2048게임

import sys

sys.stdin = open('input.txt')

def push(arr,N,mode):
    cnt = 1
    if mode == 'right':
        for i in range(N):
            for j in range(N-1,0,-1):
                cnt = 1
                if arr[i][j] == 0:
                    while 1:
                        if arr[i][j-cnt] != 0:
                            arr[i][j] = arr[i][j-cnt]
                            arr[i][j-cnt] = 0
                            break
                        cnt += 1
                        if j - cnt < 0:
                            break
  
    elif mode == 'left':
        for i in range(N):
            for j in range(N-1):
                cnt = 1
                if arr[i][j] == 0:
                    while 1:
                        if arr[i][j+cnt] != 0:
                            arr[i][j] = arr[i][j+cnt]
                            arr[i][j+cnt] = 0
                            break
                        cnt +=1
                        if j + cnt > N - 1:
                            break
                        
    elif mode == 'up':
        for i in range(N-1):
            for j in range(N):
                cnt = 1
                if arr[i][j] == 0:
                    while 1:
                        if arr[i+cnt][j] != 0:
                            arr[i][j] = arr[i+cnt][j]
                            arr[i+cnt][j] = 0
                            break
                        cnt += 1
                        if i+cnt > N - 1:
                            break
                        
                
    elif mode == 'down':
        for i in range(N-1,0,-1):
            for j in range(N):
                cnt = 1
                if arr[i][j] == 0:
                    while 1:
                        if arr[i-cnt][j] != 0:
                            arr[i][j] = arr[i-cnt][j]
                            arr[i-cnt][j] = 0
                            break
                        cnt += 1
                        if i - cnt < 0:
                            break

    return arr 

def merge(arr,N,mode):
    if mode == 'right':
        for i in range(N):
            for j in range(N-1,0,-1):
                if arr[i][j] == arr[i][j-1]:
                    arr[i][j] = arr[i][j] + arr[i][j-1]
                    arr[i][j-1] = 0

                    

    elif mode == 'left':
        for i in range(N):
            for j in range(N-1):
                if arr[i][j] == arr[i][j+1]:
                    arr[i][j] = arr[i][j] + arr[i][j+1]
                    arr[i][j+1] = 0

    elif mode == 'up':
        for i in range(N):
            for j in range(N-1):
                if arr[j][i] == arr[j+1][i] :
                    arr[j][i] = arr[j][i] + arr[j+1][i]
                    arr[j+1][i] = 0
                
    elif mode == 'down':
        for i in range(N):
            for j in range(N-1,0,-1):
                if arr[j][i] == arr[j-1][i] :
                    arr[j][i] = arr[j][i] + arr[j-1][i]
                    arr[j-1][i] = 0
    return arr 

T = int(input())
for tc in range(1, T+1):
    c_N, mode = input().split()
    N = int(c_N)
    data = [list(map(int,input().split())) for _ in range(N)]
    d = push(data,N,mode)
    d = merge(data,N,mode)
    d = push(data,N,mode)
    print('#{}'.format(tc))
    for line in d:
        print(' '.join(map(str,line)))

    
    