# Problem [11651] : 좌표 정렬하기 2

import sys

n_val = int(sys.stdin.readline())
locations = [list(map(int,sys.stdin.readline().split())) for _ in range(n_val)]
sorted_list = list(sorted(locations,key= lambda x : (x[1],x[0])))

for axis in sorted_list:
    print('{} {}'.format(axis[0],axis[1]))