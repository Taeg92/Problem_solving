# Problem [1545] : 주어진 숫자부터 0까지 순서대로 찍어보세요

num = int(input())
num_list = list()
for i in range(num,-1,-1) :
    num_list.append(i)

string = ' '.join(map(str,num_list))
print(string)