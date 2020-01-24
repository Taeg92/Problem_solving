# Problem [1970] : 쉬운 거스름돈
# S마켓에서 손님에게 거슬러 주어야 할 금액 N이 입력되면 돈의 최소 개수로 거슬러 주기 위하여 각 종류의 돈이 몇 개씩 필요한지 출력하라.


test_cnt = int(input())
for test in range(1,test_cnt+1):
    result = ''
    result_list = [0]*8
    price = int(input())
    while(price >= 10) :
        if price >= 50000 :
            price -= 50000
            result_list[0] += 1
        elif price >= 10000 :
            price -= 10000
            result_list[1] += 1
        elif price >= 5000 :
            price -= 5000
            result_list[2] += 1
        elif price >= 1000 :
            price -= 1000
            result_list[3] += 1
        elif price >= 500 :
            price -= 500
            result_list[4] += 1    
        elif price >= 100 :
            price -= 100
            result_list[5] += 1 
        elif price >= 50 :
            price -= 50
            result_list[6] += 1
        elif price >= 10 :
            price -= 10
            result_list[7] += 1    
        
    result = ' '.join(map(str,result_list))
    print('#{}\n{}'.format(test,result))