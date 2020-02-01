# Problem [1427] : 소트인사이드

import sys

num = int(sys.stdin.readline())
num_list = list(map(int,list(str(num))))
sorted_list = list(map(int,sorted(num_list,reverse=True)))

print(''.join(map(str,sorted_list)))