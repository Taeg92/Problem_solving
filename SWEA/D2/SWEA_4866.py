# Problem [4866] : 괄호 검사

T = int(input())
for tc in range(1,T+1):
    result = '1'
    data = list(input())
    bracket = ['{', '}', '(', ')']
    d = list()
    for i in range(len(data)):
        if data[i] in bracket:
            d.append(data[i])
    i = 0
    flag = 0
    if len(d) <= 1 :
        result = '0' 
    else:
        while len(d) != 0:
            if d[i] == '{':
                if d[i+1] == '}':
                    d.pop(i)
                    d.pop(i)
                    flag = 1
            elif d[i] == '(':
                if d[i+1] == ')':
                    d.pop(i)
                    d.pop(i)
                    flag = 1
            i += 1
            if flag == 1 and i >= len(d) - 1:
                i = 0
                flag = 0
            if flag == 0 and i == len(d) - 1:
                result = '0'
                break
    print('#{} {}'.format(tc,result))