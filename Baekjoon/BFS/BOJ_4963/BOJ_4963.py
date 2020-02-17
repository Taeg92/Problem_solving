# Problem [4963] : 섬의 개수

import sys
sys.stdin = open('input.txt')


while 1:
    w, h = map(int,input().split())
    if not w and not h:
        break
    data = [list(map(int,input().split())) for _ in range(h)]
    