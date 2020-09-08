def getIndex(query):
    flag = False
    cnt = 0
    for i in range(len(query)):
        if query[i] == '?':
            if flag:
                cnt += 1
            else:
                cnt += 1
                startIndex = i
                flag = True

    return startIndex, cnt

def solution(words, queries):
    
    answer = list()

    for query in queries:
        s, size = getIndex(query)
        cnt = 0
        for word in words:
            if len(word) != len(query):
                continue
            if s == 0:
                if word[size:] == query[size:]:
                    cnt += 1
            else:
                if word[:s] == query[:s]:
                    cnt += 1

        answer.append(cnt)
    
    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]

print(solution(words, queries))