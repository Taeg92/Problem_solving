import sys
sys.stdin = open('input.txt')

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int,input().split())
        D = list(map(int,input().split()))
        Q = list()
        
        for i in range(N):
            Q.append([i, D[i]])

        i = 0
        while len(Q) != 1:
            Q[0][1] //= 2

            if Q[0][1] == 0:
                if N + i < M:
                    Q.pop(0)
                    Q.append([i+N, D[i+N]])
                    i += 1
                else:
                    Q.pop(0)
            else:
                Q.append(Q.pop(0))
        print(f'#{tc} {Q[0][0]+1}')