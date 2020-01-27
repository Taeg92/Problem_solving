# Problem [1229] : 암호문 3
# 규칙에 맞게 작성된 명령어를 나열하여 만든 문자열이 주어졌을 때, 암호문을 수정하고, 수정된 결과의 처음 10개 숫자를 출력하는 프로그램을 작성하여라.
# 첫번쨰 줄 입력 : 원본 암호문의 길이 N (10 <= N <= 20)
# 두번째 줄 입력 : 원본 암호문
# 세번째 줄 입력 : 명령어의 개수 (5 <= N <= 10)
# 네번째 줄 입력 : 명령어
# 출력 : #기호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 수정된 암호문의 처음 10개항을 출력한다.


for test in range(1,11) :
    len_password = int(input())
    origin_password = list(map(int,input().split()))
    command_cnt = int(input())
    command = list(input().split())
    for _ in range(command_cnt) :
        command_type = command.pop(0)
        if command_type == 'I':
            start = int(command.pop(0))
            size = int(command.pop(0))
            for i in range(size) :
                origin_password.insert(start+i,command.pop(0))
        elif command_type == 'D':
            delete_idx = int(command.pop(0))
            delete_cnt = int(command.pop(0))
            for _ in range(delete_cnt) :
                origin_password.pop(delete_idx)
        if command_type == 'A':
            size = int(command.pop(0))
            for _ in range(size) :
                origin_password.insert(-1,command.pop(0))
    string = ' '.join(map(str,origin_password[:10]))
    print('#{} {}'.format(test,string))