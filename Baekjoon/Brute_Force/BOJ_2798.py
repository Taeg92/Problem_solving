# Problem [2798] : 블랙잭
# 첫째줄 입력으로 카드의 개수와 세카드 합의 최대값 M을 입력한다.
# 둘째줄 입력으로 각 카드의 숫자를 입력 받는다.

card_cnt, blackjack = map(int,input().split())
cards = list(map(int,input().split()))

max_sum = 0
num_sum = 0
for i in range(len(cards)):
    for j in range(len(cards)):
        if cards[i] != cards[j]:
            for k in range(len(cards)):
                if cards[j] != cards[k] and cards[i] != cards[k] :
                    num_sum = cards[i]+cards[j]+cards[k]
                    if num_sum > max_sum and num_sum <= blackjack :
                        max_sum = num_sum
print(max_sum)

