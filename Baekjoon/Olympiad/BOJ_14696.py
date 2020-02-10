# Problem [14696] : 딱지놀이
# 별(4) > 동그라미(3) > 네모(2) > 세모(1) > 무승부


# 라운드
N = int(input())

# A가 내는 딱지에 나온 그림의 총 개수 a , 딱지에 나온 그림

for tc in range(N):
    data_A = list(map(int,input().split()))
    data_B = list(map(int, input().split()))
    temp_A = data_A[1:]
    temp_B = data_B[1:]
    result = 'D'
    temp = list()
    for i in range(4,-1,-1):
        temp.append(temp_A.count(i)-temp_B.count(i))

    for n in temp:
        if n > 0:
            result = 'A'
            break
        elif n < 0 :
            result = 'B'
            break
        else:
            pass
    print(result)