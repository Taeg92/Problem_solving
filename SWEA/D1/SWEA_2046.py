# Problem [2046] : 주어진 숫자만큼 # 을 출력해보세요.
# 주어질 숫자는 100,000 이하다.

cnt = int(input())
string = ''

for i in range(cnt):
    string += '#'
    
print(string)
