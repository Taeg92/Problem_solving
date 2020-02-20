# Problem [4880] : 토너먼트 게임

def tournament(arr):
    if len(arr)==1:
        return arr
    elif len(arr)==2:
        if arr[0][1]==arr[1][1]:
            return [arr[0]]
        else:
            if (arr[0][1])%3 +1 ==arr[1][1]:
                return [arr[1]]
            else:
                return [arr[0]]
    else:
        t1= tournament(arr[:(len(arr)+1)//2])
        t2= tournament(arr[(len(arr)+1)//2:])
        return tournament(t1+t2)

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    d = list(map(int,input().split()))
    heap = list()
    for i in range(len(d)):
        heap.append([i+1,d[i]])
    result = tournament(heap)
    print('#{} {}'.format(tc,result[0][0]))


