# Problem [1936] : 1대1 가위바위보 
# 가위 : 1 , 바위 : 2, 보 : 3

num = list(map(int,input().split()))


if (num[0] > num[1]) :
    if(num[0] == 3 and num[1] == 1) :
        print('B')
    else :
        print('A')
elif (num [0] < num[1]) :
    if(num[0] == 1 and num[1] == 3) :
        print('A')
    else :
        print('B')
        

