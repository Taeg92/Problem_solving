#Problem [9633] : N-Queen

def isTrue(n):
    for past_idx in range(n):
        if row[n] == row[past_idx] or abs(row[n]-row[past_idx]) == n-past_idx:
            return False
    return True 

def Queen(n):
    global result
    if n == N:
        result += 1

    else:
        for i in range(N):
            row[n] = i
            if isTrue(n):
                Queen(n+1)

N = int(input())
row = [0]*15
result = 0
Queen(0)
print(result)