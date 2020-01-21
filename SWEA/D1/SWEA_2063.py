# Problem[2063] : 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
# 입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력하라.
# N은 항상 홀수로 주어진다.
# N은 9이상 199이하의 정수이다(9 <= N <= 199)


test_cnt = int(input())
num_list = list(map(int,input().split()))
result = sorted(num_list)

print("{}".format(result[(test_cnt//2)]))