# Problem [1210] : Ladder1

for tc in range(1,11):
    T= int(input())
    data = [list(map(int,input().split())) for _ in range(100)]
    end = [(99,i) for i in range(100) if data[99][i] == 2]
    i = end[0][0]
    j = end[0][1]
    while i != 0:
        if j+1 <= 99 and data[i][j+1] == 1:
            while data[i][j+1] == 1:
                j += 1
                if j == 99:
                    break
            i -= 1
        elif j-1 >= 0 and data[i][j-1] == 1:
            while data[i][j-1] == 1:
                j -= 1
                if j == 0:
                    break
            i -= 1
        else:
            i -= 1
        
    print('#{} {}'.format(T,j))