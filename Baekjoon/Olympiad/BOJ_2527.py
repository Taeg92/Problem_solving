# Problem [2527] : 직사각형

for tc in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int,input().split())
    result = ''
    if x1 < x2 and p1 < p2 and y1 < y2 and q1 < q2 :
        result = 'a'
