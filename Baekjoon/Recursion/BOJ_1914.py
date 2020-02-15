# Problem [1914] : 하노이 탑

def hanoi_cnt(N):
    if N == 1:
        return 1
    else :
        return 2*hanoi_cnt(N-1) + 1
    
def print_hanoi(N,start,temp,end):
    if N == 1:
        print(start, end)
    else:
        print_hanoi(N-1,start,end,temp)
        print(start,end)
        print_hanoi(N-1,temp,start,end)


N = int(input())
cnt = hanoi_cnt(N)
if N <= 20:
    print(cnt)
    print_hanoi(N,1,2,3)
else:
    print(cnt)