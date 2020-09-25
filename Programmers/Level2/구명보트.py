def solution(people, limit):
    answer = len(people)
    people = sorted(people, reverse = True)
    s,e = 0, len(people)-1
    while s < e : 
        if people[s]+people[e] <= limit :
            e-=1
            answer-=1
        s+=1
    return answer

people = [70, 50, 80, 50]
limit = 100

print(solution(people, limit))