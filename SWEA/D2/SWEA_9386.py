# Problem [9386] : 연속한 1의 개수

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = input().split('0')
    m = 0
    for data in d:
        if len(data) > m:
            m = len(data)
    print('#{} {}'.format(tc,m))