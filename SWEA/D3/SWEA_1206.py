# Problem [1206] : View
# 왼쪽과 오른쪽에 조망권 2칸이상 학보된 빌딩 세알리기.
# 빌딩의 높이의 최대는 255이다.

for test in range(1, 11):
    n_value = int(input())
    buildings = list(map(int,input().split()))
    result = 0
    for i in range(2,n_value-2) :
        max_neighbor = max(buildings[i-2],buildings[i-1],buildings[i+1],buildings[i+2])
        if(buildings[i] > max_neighbor) :
            result += buildings[i] - max_neighbor
    print('#{} {}'.format(test,result))