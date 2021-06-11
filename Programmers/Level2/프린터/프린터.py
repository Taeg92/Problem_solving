def solution(priorities, location):

    answer = 0
    val = priorities[location]
    priorities[location] = 0

    while priorities:
        temp = priorities.pop(0)
        if priorities:
            if temp == 0:
                if val >= max(priorities):
                    answer += 1 
                    return answer
                else:
                    priorities.append(temp)
            else:
                if temp >= val and temp >= max(priorities) :
                    answer += 1
                else:
                    priorities.append(temp)
        else:
            return answer+1
    

priorities = [1, 1, 9, 1, 1, 1]
location = 0
print(solution(priorities, location))