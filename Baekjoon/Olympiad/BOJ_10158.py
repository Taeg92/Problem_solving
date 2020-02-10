# Problem [10158] : 개미

w, h = map(int,input().split())
x, y = map(int,input().split())
time = int(input())

if (y+time)//h % 2 == 1:
    y = h - (y+time) % h
else:
    y = (y+time) % h

if (x+time)//w % 2 == 1:
    x = w - (x+time) % w
else:
    x = (x+time) % w


print(x,y)