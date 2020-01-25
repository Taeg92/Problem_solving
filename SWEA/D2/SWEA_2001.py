# Problem [2001] : 파리퇴치
# N X N 배열 안의 숫자는 해당 영역에 존재하는 파리의 개수를 의미한다.
# M X M 크기의 파리채를 한 번 내리쳐 최대한 많은 파리를 죽이고자 한다.
# 죽은 파리의 최대 개수를 구하라.


def numFly(arr,map_size,flapper_size):  
    result = list()
    for start_point_width in range(0,map_size-flapper_size+1):
        for start_point_height in range(0,map_size-flapper_size+1):
            sum_rec = 0
            for rec_width in range (flapper_size):
                for rec_height in range(flapper_size):
                    sum_rec += arr[start_point_width+rec_width][start_point_height+rec_height]
            result.append(sum_rec)

    return max(result)

test_cnt = int(input())   

for test in range(1, test_cnt+1):

    map_size, flapper_size = map(int,input().split())
    matrix = [list(map(int,input().split())) for _ in range(map_size)]
    result = numFly(matrix,map_size,flapper_size)

    print('#{} {}'.format(test,result))