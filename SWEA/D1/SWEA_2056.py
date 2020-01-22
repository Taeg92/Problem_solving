# Problem[2056] : 연월일 순으로 구성된 8자리의 날짜가 입력으로 주어진다. 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력
# 단, 날짜가 유효하지 않다면 -1을 출력

def isDate(a, b) :    

    if (int(a) not in range(1,13)) :
            return False
    elif (int(a) == 2) :
        if(int(b) not in range (1,29)) :
            return False
        else :
            return True
    elif (int(a) == 1 or int(a) == 3 or int(a) == 5 or int(a) == 7 or int(a) ==8 or int(a) ==10 or int(a) == 11) :
        if(int(b) not in range(1,32)) :
            return False
        else :
            return True
    elif (int(a) == 4 or int(a) == 6 or int(a) == 9 or int(a) == 12) :
        if(int(b) not in range(1,31)) :
            return False
        else :
            return True

test_cnt = int(input())
result_list = list()
result_list = [0]*test_cnt

for index in range(test_cnt):
    date_input = input()
    year = date_input[0:4]
    month = date_input[4:6]
    date = date_input[6:8]
    
    result = isDate(month,date)
    if result == True:
        string = year + '/' + month + '/' + date
        result_list[index] = string
    elif result == False :
        string = '-1'
        result_list[index] = string
        
for idx,result in enumerate(result_list):
    print("#{} {}".format(idx+1,result))
    