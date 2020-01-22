# Problem[2050] : 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
# 문자열의 최대 길이는 200이다.

# ASCII code : A = 65 , Z = 90

string = input()
Alpha_dict = dict()
result = list()
for i in string :
    if i not in Alpha_dict :
        Alpha_dict[i] = ord(i) - 64

for value in Alpha_dict.values() :
    result.append(value)

result_string = ' '.join(map(str,result))

print(result_string)