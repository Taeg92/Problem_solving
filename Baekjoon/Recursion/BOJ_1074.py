# Problem [1074] : Z
import sys

n = 0
def recursion_Z(x, y, size):
    global n
    # 종료조건
    if x == r and y == c:
        print(n)
        return

    # 재귀
    if x <= r < x + size and y <= c < y + size:
        recursion_Z(x,y,size//2)
        recursion_Z(x,y+size//2,size//2)
        recursion_Z(x+size//2,y,size//2)
        recursion_Z(x+size//2,y+size//2,size//2)
    else:
        n += size*size



N, r, c = map(int, input().split())
recursion_Z(0,0,2**N)
