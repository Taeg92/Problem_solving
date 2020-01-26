# Problem [1004] : 어린왕자
# 출발점, 도착점이 주어졌을 때 어린왕자에게 필요한 최소의 행성 진입/이탈수 구하기.
# 입력의 첫 줄에는 테스트 케이스 T
# 그 다음 줄부터는 각각의 테스트 케이스에 적용 될 시작점 출발점
# 행성의 계수 n 입력
# n 줄에 걸쳐 행성계의 중점과 반지름 입력


test_cnt = int(input())
for test in range(test_cnt) :
    x1, y1, x2, y2 = map(int,input().split())
    n = int(input())
    count = 0
    for i in range(n) :
        c_x, c_y, r = map(int,input().split())
        if (x1-c_x)**2 + (y1-c_y)**2 <= r**2 and (x2-c_x)**2 + (y2-c_y)**2 <= r**2 :
            count += 1 
        elif(x1-c_x)**2 + (y1-c_y)**2 > r**2 and (x2-c_x)**2 + (y2-c_y)**2 <= r**2 :
            count += 1
        elif(x1-c_x)**2 + (y1-c_y)**2 <= r**2 and (x2-c_x)**2 + (y2-c_y)**2 > r**2 :
            count += 1
    print(count)
            