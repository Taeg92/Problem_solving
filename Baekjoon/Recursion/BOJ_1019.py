# Problem [1019] : 책 페이지

N = int(input())
arr = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in range(1,N+1):
    while i:
        arr[i%10] += 1
        i //= 10
print(*arr)