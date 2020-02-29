# Problem [5658] : 보물상자 비밀번호 

from collections import deque
import sys
sys.stdin = open('input.txt')


if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, K = map(int,input().split())
        D = deque(input())
        result = list()
        size = N // 4
        for _ in range(N//4):
            for i in range(4):
                token = ''.join(map(str,list(D)[i*size:(i+1)*size]))
                num = int(token,16)
                if num not in result:
                    result.append(num)
            D.appendleft(D.pop()) 
        result = sorted(result,reverse=True)
        print('#{} {}'.format(tc,result[K-1]))