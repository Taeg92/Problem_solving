# Problem [2527] : 직사각형

for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,input().split())
    result = ''

    if x1 > x2 :
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        p1, p2 = p2, p1
        q1, q2 = q2, q1

    if p1 < x2 :
        result = 'd'
    elif p1 == x2:
        if q2 < y1 :
            result = 'd'
        elif q2 == y1 :
            result = 'c'
        elif y1 < q2 < q1:
            result = 'b'
        elif q2 == q1:
            result = 'b'
        elif q2 > q1:
            if y2 < q1 :
                result = 'b'
            elif y2 == q1:
                result = 'c'
            else:
                result = 'd'

    elif x2 < p1 and  p1 < p2:
        if q2 < y1 :
            result = 'd'
        elif q2 == y1 :
            result = 'b'
        elif y1 < q2 < q1:
            result = 'a'
        elif q2 == q1:
            result = 'a'
        elif q2 > q1:
            if y2 < q1 :
                result = 'a'
            elif y2 == q1:
                result = 'b'
            else:
                result = 'd'
    elif x1 < x2 < p1 and x1 < p2 < p1:
        if q2 < y1 :
            result = 'd'
        elif q2 == y1 :
            result = 'b'
        elif y1 < q2 < q1:
            result = 'a'
        elif q2 == q1:
            result = 'a'
        elif q2 > q1:
            if y2 < q1:
                result = 'a'
            elif y2 == q1:
                result = 'b'
            else:
                result = 'd'
    elif x1 == x2 and p1 < p2 :
        if q2 < y1 :
            result = 'd'
        elif q2 == y1 :
            result = 'b'
        elif y1 < q2 < q1:
            result = 'a'
        elif q2 == q1:
            result = 'a'
        elif q2 > q1:
            if y2 < q1:
                result = 'a'
            elif y2 == q1:
                result = 'b'
            else:
                result = 'd'
    elif x1 == x2 and p2 < p1:
        if q2 < y1 :
            result = 'd'
        elif q2 == y1 :
            result = 'b'
        elif y1 < q2 < q1:
            result = 'a'
        elif q2 == q1:
            result = 'a'
        elif q2 > q1:
            if y2 < q1:
                result = 'a'
            elif y2 == q1:
                result = 'b'
            else:
                result = 'd'
    else:
        if q2 < y1 :
            result = 'd'
        elif q2 == y1 :
            result = 'b'
        elif y1 < q2 < q1:
            result = 'a'
        elif q2 == q1:
            result = 'a'
        elif q2 > q1:
            if y2 < q1:
                result = 'a'
            elif y2 == q1:
                result = 'b'
            else:
                result = 'd'
    print(result)