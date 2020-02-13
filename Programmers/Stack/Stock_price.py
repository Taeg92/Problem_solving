# Problem : 주식 가격

def solution(prices):
    answer = []

    for i in range(len(prices)):
        cnt = 0
        for j in range(i+1,len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        answer.append(cnt)
    return answer



prices = [1, 2, 3, 2, 3]
print(solution(prices))

#[10,9,8,7,5,3,1,1,1,1,0]
prices = [1,2,3,4,5,6,7,6,5,4,3]
print(solution(prices))
