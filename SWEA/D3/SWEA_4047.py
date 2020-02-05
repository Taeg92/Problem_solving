# 4047. 영준이의 카드 카운팅
# 입력 : 가지고 있는 카드의 무늬 종류와 카드 숫자를 입력
# 각 무늬별로 13장의 카드를 만드는 데 부족한 카드 수를 출력

def my_card(cards):
    my_card = [[] for _ in range(4)]
    result = list()
    for card in cards:
        if card[0] == 'S':
            num = int(''.join(map(str,card[1])))
            if num not in my_card[0]:
                my_card[0].append(num)
            else :
                return 'ERROR'
        elif card[0] == 'D':
            num = int(''.join(map(str,card[1])))
            if num not in my_card[1]:
                my_card[1].append(num) 
            else :
                return 'ERROR' 
        elif card[0] == 'H':
            num = int(''.join(map(str,card[1])))
            if num not in my_card[2]:
                my_card[2].append(num)
            else :
                return 'ERROR'
        elif card[0] == 'C':
            num = int(''.join(map(str,card[1])))
            if num not in my_card[3]:
                my_card[3].append(num)
            else :
                return 'ERROR'
    for c in my_card:
        result.append(13-len(c))
    result = ' '.join(map(str,result))
    return result
    

T = int(input())
for tc in range(1, T+1):
    data = input()
    data = data.replace('A','01')
    data = data.replace('J','11')
    data = data.replace('Q','12')
    data = data.replace('K','13')
    cards = [[data[i], data[i+1:i+3]] for i in range(0, len(data), 3)]
    result = my_card(cards)
    print('#{} {}'.format(tc,result))

