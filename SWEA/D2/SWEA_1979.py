# Problem [1979] : 어디에 단어가 들어갈 수 있을까
# N X N 크기의 단어 퍼즐에 입력으로 단어 퍼즐의 모양이 주어진다.
# 1이 써진 칸에 단어가 들어갈 수 있다.
# N : 퍼즐의 크기(가로,세로의 길이) , K 단어의 길이

def check_space(arr,size,w_length):
    count = 0
    col_list = list()
    row_list = list()
    total_list = list()
    for i in range(size) :
        string = ''
        for j in range(size) :
            string += str(arr[i][j])
        row_list.append(string)
    for i in range(size):
        string = ''
        for j in range(size) :
            string += str(arr[j][i])
        col_list.append(string)

    total_list = row_list
    total_list.extend(col_list)   

    for line in total_list:
        result = line.split('0')
        for i in range(len(result)):
            if result[i] == '1'*w_length :
                count += 1
    return count

        
    

test_cnt = int(input())   
for test in range(1, test_cnt+1):
    size, w_length = map(int,input().split())
    matrix = [list(map(int, input().split())) for _ in range(size)]
    result = check_space(matrix,size,w_length)
    print('#{} {}'.format(test,result))
