# Problem [2007] : 패턴 마디의 길이
# 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램.
# 각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.

def find_Pattern(string) :
    word = ''
    for i in string :
        word += i
        if word[0:len(word)//2] == word[len(word)//2:] :
            return len(word[0:len(word)//2])
    
test_cnt = int(input())

for test in range(1,test_cnt+1) :
    string = input()
    result = find_Pattern(string)
    print('#{} {}'.format(test,result))