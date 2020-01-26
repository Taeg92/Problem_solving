# Problem [1208] : Flatten
# 높은 곳의 상자를 낮은 곳에 옮기는 방식으로 최고점과 최저점의 간격을 줄이는 작업
# 가로 길이는 항상 100
# 덤프 횟수는 입력으로 주어짐 1 <= count <= 1000


for test in range(10) :
    d = int(input())
    h = list(map(int, input().split()))
    count = 0
    while True :
        h[h.index(max(h))] -= 1
        h[h.index(min(h))] += 1
        count += 1
        if(count == d) :
            break
    print('#{} {}'.format(test+1,max(h)-min(h)))
