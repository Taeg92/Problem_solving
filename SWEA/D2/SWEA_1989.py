# Problem [1989] : 초심자의 회문 검사
# 거꾸로 읽어도 제대로 읽은 것과 같은 문장 찾기
# 각 단어의 길이는 3 이상 10 이하.

def isPalindrome(string) :

    string_list = list(string)
    reverse_string = list(reversed(string_list))
    if string_list == reverse_string :
        return 1
    return 0   

test_num = int(input())

for test in range(1,test_num+1) :
    
    string = input()
    result = isPalindrome(string)
    print('#{} {}'.format(test,result))