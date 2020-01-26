# Problem [1244] : 스위치 켜고 끄기
# 스위치 1 : On 스위치 0 : off
# 스위치는 1번부터 8번까지 번호가 붙어있다.
# 남학생 : 자기가 받은 수의 배수에 해당하는 번호를 받은 스위치를 켜거나 끈다.
# 여학생 : 자기가 받은 번호를 기준으로 상태가 같은 가장 긴 대칭의 스위치를 포함하여 사이의 스위치의 상태를 바꾼다.
# 입력 첫째줄에는 스위치의 개수
# 두번쨰 줄에는 스위치의 상태
# 세번째 줄부터는 학생의 성별과 학생이 받을 숫자를 입력한다.
# 남자 : 1 여자 : 2

num_switch = int(input())
switchs = list(map(int,input().split()))
num_students = int(input())
student = [list(map(int,input().split())) for _ in range(num_students)]

for student in student :
    if student[0] == 1 :
        for i in range(num_switch) :
            if (i+1) % student[1] == 0 :
                if switchs[i] == 0 :
                    switchs[i] = 1 
                else :
                    switchs[i] = 0
    if student[0] == 2:  
        if switchs[student[1]-1] == 0 :
            switchs[student[1]-1] = 1
        else :
            switchs[student[1]-1] = 0
        count = 1
        while (student[1] + count < num_switch + 1) and (student[1] - count > 0) and (switchs[(student[1]-1)-count] == switchs[(student[1]-1)+count]) :
            if switchs[(student[1]-1)-count] == 1 :
                switchs[(student[1]-1)-count] = 0
                switchs[(student[1]-1)+count] = 0
            elif switchs[(student[1]-1)-count] == 0 :
                switchs[(student[1]-1)-count] = 1
                switchs[(student[1]-1)+count] = 1
            count += 1
for idx, switch in enumerate(switchs) :
    if idx and not(idx % 20):
        print()
    print(switch, end = ' ')