# Problem [4012] : [모의 SW 역량테스트] 요리사

from itertools import combinations as combi
import sys
sys.stdin = open('input.txt')


if __name__ == '__main__':
    T = int(input())
    for tc in range(1, T+1):
        N = int(input())
        D = [list(map(int,input().split())) for _ in range(N)]
        m = float('inf')
        food = list(combi(range(N),N//2))

        for food1 in food:
            food2 = list()
            for n in range(N):
                if n not in food1:
                    food2.append(n)
            s1 = 0
            for i in range(N//2):
                for j in range(i+1,N//2):
                    s1 += D[food1[i]][food1[j]] + D[food1[j]][food1[i]]
            s2 =0
            for i in range(N//2):
                for j in range(i+1,N//2):
                    s2 += D[food2[i]][food2[j]] + D[food2[j]][food2[i]]
            m = min(m,abs(s2-s1))
        print('#{} {}'.format(tc, m))