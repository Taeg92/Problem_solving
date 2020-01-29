# Problem [1289] : 원재의 메모리 복구하기
# 첫 번째 줄에 테스트 케이스 수 T
# 다음 줄에 각 테스트 케이스는 한 줄로 이루어짐
# 메모리 길이는 1이상 50 이하


test_cnt = int(input())
for test in range(1,test_cnt+1):
    memory = input()
    arr = list(str(memory))
    count = 0
    for idx in range(len(memory)-1) :
        if idx == 0 and memory[0] == '1':
            count += 1
        if memory[idx] != memory[idx+1]:
            count += 1
    print('#{} {}'.format(test,count))