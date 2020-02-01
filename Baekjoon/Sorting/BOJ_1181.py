# Problem [1181] : 단어 정렬

n_val = int(input())
words = [list(input()) for _ in range(n_val)]
result = list()
for word in words:
    if word not in result:
        result.append(word)

sorted_list = list(sorted(result,key = lambda x : (len(x),x)))


for word in sorted_list:
    print(''.join(map(str,word)))