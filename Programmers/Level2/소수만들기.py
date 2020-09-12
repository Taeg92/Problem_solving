from itertools import combinations

def isPrime(n):
    if n < 2: 
        return False 
    for i in range(2, int(n**0.5)+1): 
        if not n % i: 
            return False 
    return True
    

def solution(nums):
    answer = 0
    for comb in combinations(nums, 3):
        if isPrime(sum(comb)):
            answer +=1
    return answer

nums = [1,2,7,6,4]
print(solution(nums))