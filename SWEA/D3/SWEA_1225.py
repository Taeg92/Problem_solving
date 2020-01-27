# Problem [1225] : 7일차 - 암호생성기
# 8개의 숫자를 입력 받는다
# 첫번쨰 숫자를 1감소 한 뒤, 맨 뒤로 보낸다.
# 다음 첫 번째 수는 2 감소한 뒤 맨 뒤로 보낸다..... 숫자가 감소할 때 0보다 작아지는 경우 0으로 유지하고 프로그램 종료.


for test in range(10) :
    test_case = int(input())
    password = list(map(int,input().split()))
    cnt = 1
    while True :
        password.append(password.pop(0)-cnt)
        if password[-1] <= 0 :
            password[-1] = 0
            break
        cnt += 1
        if cnt == 6 :
            cnt = 1
    string = ' '.join(map(str,password))
    print('#{} {}'.format(test_case,string))