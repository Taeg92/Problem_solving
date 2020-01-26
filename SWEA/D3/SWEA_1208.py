# Problem [1208] : Flatten
# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업
# 가로 길이는 항상 100
# 덤프 횟수는 입력으로 주어짐 1 <= count <= 1000


for test in range(1,11) :
    dump_val = int(input())
    height_list = list(map(int,input().split()))
    for __ in range(dump_val) :
        height_list[height_list.index(height_list)] -= 1
        height_list[height_list.index(min(height_list))] += 1
    result = max(height_list) - min(height_list)
    print('#{} {}'.format(test,max(height_list) - min(height_list)))


    # for t in range(10):
    # n = int(input())
    # h = list(map(int, input().split()))
    # for _ in range(n):
    #     h[h.index(max(h))] -= 1
    #     h[h.index(min(h))] += 1
    # print(f'#{t+1} {max(h)-min(h)}')