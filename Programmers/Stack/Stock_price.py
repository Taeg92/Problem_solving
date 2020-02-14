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

# code 1
# def solution(prices):
#     answer = []
#     for i in range(len(prices)):
#         cnt = 0
#         for j in range(i+1,len(prices)):
#             cnt += 1
#             if prices[i] > prices[j]:
#                 break
#         answer.append(cnt)
#     return answer

# code 2
# def solution(prices):
#     stack = []
#     result = [0 for _ in range(len(prices))]
#     for i in range(len(prices)):
#         while stack and prices[stack[-1]] > prices[i]:
#             x = stack.pop()
#             result[x] = i - x
#         stack.append(i)
#     while stack:
#         x = stack.pop()
#         result[x] = i - x
#     return result


prices = [1, 2, 3, 2, 3]
print(solution(prices))

#[10,9,8,7,5,3,1,1,1,1,0]
prices = [1,2,3,4,5,6,7,6,5,4,3]
print(solution(prices))
