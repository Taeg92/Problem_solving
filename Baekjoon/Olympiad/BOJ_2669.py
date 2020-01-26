# Problem [2669] : 직사각형 네개의 합집합의 면적 구하기
# 입력은 네 줄,  각 줄은 직사각형의 위치를 나타내는 네 개의 정수로 주어진다.
# 입력 = x1 y1 x2 y2
# 모든 좌표는 1이상 100이하의 정수이다.


matrix = [[0 for _ in range(101)] for _ in range(101)]
result = 0
for _ in range(4) :
    x1, y1, x2, y2 = map(int,input().split())
    for x in range(x1,x2) :
        for y in range(y1,y2) :
            if matrix[x][y] != 1 :
                matrix[x][y] = 1
                result += 1          
print(result)