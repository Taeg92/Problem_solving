# Problem [13300] : 방 배정
# 여학생 => 0 남학생 => 1
# 성별 , 학년으로 입력

grade = [[0,0] for _ in range(7)]
N, K = map(int,input().split())
students = [list(map(int,input().split())) for _ in range(N)]
cnt = 0

for student in students:
    if student[0] == 1:
        grade[student[1]][1] += 1
    else:
        grade[student[1]][0] += 1

for i in range(1,len(grade)):
    for j in range(2):
        if grade[i][j] > K:
            if grade[i][j] % K != 0:
                cnt += grade[i][j]//K + 1
            else:
                cnt += grade[i][j]//K
        elif 1 <= grade[i][j] <= K:
            cnt += 1
        else:
            pass
print(cnt)