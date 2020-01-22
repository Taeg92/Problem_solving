# Problem [1288] : 새로운 불면증 치료법
# 0부터 9까지 모든 일의 자릿수를 확인하면 종료


test_cnt = int(input())

for test in range(test_cnt):
    n_value = int(input())
    num_list = set()
    cnt = 0
    while True:
        cnt += 1
        val = n_value*cnt
        while(val > 0) :
            num_list.add(val % 10)
            val = val//10
        if (len(num_list) == 10) :
            break
    result = cnt * n_value
    print('#{} {}'.format(test+1,result))