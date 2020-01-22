# problem [1204] : 최빈수 구하기
# 고등학교 1000명의 수학성적을 토대로 최빈수 구하기
# 학생의 수는 1000명이며, 각 학생의 점수는 0점 이상 100점 이하의 값이다.


test_cnt =int(input())

for i in range(test_cnt):
    test_num = int(input())
    score_list = list(map(int,input().split()))
    score_dict = dict()
    result = list()
    for score in score_list:
        if (score  in score_dict) :
            score_dict[score] += 1
        else :
            score_dict[score] = 1
    for score,count in score_dict.items():
        if count == max(score_dict.values()) :
            result.append(score)
    
    print('#{} {}'.format(test_num,max(result)))