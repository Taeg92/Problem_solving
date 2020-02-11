# Problem [14888] : 연산자 끼워넣기

def permutation(arr,r):
    result = list()
    arr = sorted(arr)
    used = [0]*len(arr)

    def generate(chosen,used):


        if len(chosen) == r:
            result.append(chosen[:])

        for i in range(len(arr)):
            if not used[i]:
                chosen.append(arr[i])
                used[i] = 1
                generate(chosen,used)
                used[i] = 0
                chosen.pop()
    generate([],used)
    return result


operator = ['+', '-', '*', '//']

N = int(input())
data = list(map(int,input().split()))
num_oper = list(map(int,input().split()))
m = list()
oper = list()
for i in range(4):
    if num_oper[i] != 0:
        for _ in range(num_oper[i]):
            oper.append(operator[i])

choice = permutation(oper,N-1)
for c in choice:
    s = data[0]
    for i in range(N-1):
        if c[i] == '+':
            s = s + data[i+1]
        elif c[i] == '-':
            s = s - data[i+1]
        elif c[i] == '*':
            s = s * data[i+1]
        else:
            s = abs(s) // data[i + 1]
    m.append(s)

print(max(m))
print(min(m))
