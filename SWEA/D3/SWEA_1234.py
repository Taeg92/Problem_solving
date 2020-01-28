# Problem [1234] : 비밀번호
# 0~ 9로 이루어진 번호 문자열에서 같은 번호로 붙어있는 쌍들을 소거하고 남은 번호를 비밀번호로 만든다.
# 번호 쌍이 소거되고 소거된 번호 쌍의 좌우 번호가 같은 번호이면 또 소거 할 수 있습니다.

for test in range(1,11) :
    num_cnt, num = input().split()
    numbers = list(num)
    idx = 0
    flag = 0
    while True :
        if numbers[idx] == numbers[idx+1] :
            numbers.pop(idx)
            numbers.pop(idx)
            flag = 1
        idx += 1
        if flag  == 1 :
            idx = 0
            flag = 0
        if idx == len(numbers) - 1 and flag == 0 :
            break
    string = ''.join(map(str,numbers))
    print('#{} {}'.format(test,string))



