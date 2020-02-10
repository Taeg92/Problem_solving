# Problem [2605] : 줄 세우기

N = int(input())
data = list(map(int,input().split()))
temp = list()
for i in range(len(data)):
    temp.insert(data[i],i+1)
result = list(reversed(temp))
print(' '.join(map(str,result)))