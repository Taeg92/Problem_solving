# Problem [11729] : 하노이 탑 이동 순서

def hanoi_cnt(n):
    if n == 1:
        return 1
    else :
        return 2*hanoi_cnt(n-1) + 1
    
def print_hanoi(n,start,temp,end):
    if n == 1:
        print(start, end)
    else:
        print_hanoi(n-1,start,end,temp)
        print(start,end)
        print_hanoi(n-1,temp,start,end)


n_val = int(input())
print(hanoi_cnt(n_val))
print_hanoi(n_val,1,2,3)


# def hanoi(disk, start, mid, end):
#     if disk == 1:
#         print(start, end)
#     else:
#         hanoi(disk - 1, start, end, mid)
#         print(start, end)
#         hanoi(disk - 1, mid, start, end)

# total_disk = int(input())
# total_mvmt = 0

# for disk in range(total_disk):
#     total_mvmt = total_mvmt * 2
#     total_mvmt += 1

# print(total_mvmt)
# hanoi(total_disk, 1, 2, 3)