# Problem : 금속막대

import sys
sys.stdin = open('input.txt')

def can_connect(arr1,arr2):
    if arr1[0] != arr2[-1] and arr1[-1] != arr2[0]:
        return False
    return True

def connect(arr1,arr2):
    if arr1[0] == arr2[-1]:
        return arr2 + arr1
    elif arr1[-1] == arr2[0]:
        return arr1 + arr2


def nail(arr):
    for i in range(1,len(arr)):
        if len(arr) == 1 :
            return arr
        else :
            if can_connect(arr[0],arr[i]):
                arr[0] = connect(arr[0],arr.pop(i))
                nail(arr) 
             

T = int(input())    

for tc in range(1, T+1):
    n = int(input())
    d = list(map(int,input().split()))
    temp = list()
    for i in range(n):
        temp.append(d[2*i:2*i+2])

    result = ' '.join(map(str,nail(temp)[0]))
    print('#{} {}'.format(tc,result))   

