# Problem [1074] : Z

def recursion_Z(r, c):
    
    # 종료조건
    if r == 0 and c == 0:
        return 0

    # 재귀
    else:
        if r % 2 == 1:
            if c % 2 == 1:
                return recursion_Z()
            else:
        else:
            if c % 2 == 1:




N, r, c = map(int, input().split())
result = recursion_Z(r,c)
print(result)