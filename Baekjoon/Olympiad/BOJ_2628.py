# Problem [2628] : 종이 자르기
# 입력 첫째 줄 : 가로 길이, 세로 길이 [최대값: 100]
# 입력 둘째 줄 : 자르는 점선의 수 
# 입력 셋째 줄 : 가로 => 0, 세로 => 1  + 점선의 번호 ex ) 0 3 점선 번호 3을 가로로 자름

def max_area(w_list,h_list):

    w_size = len(w_list)
    h_size = len(h_list)
    m = 0
    for i in range(1,h_size):
        for j in range(1,w_size):
            area = (h_list[i]-h_list[i-1])*(w_list[j]-w_list[j-1])
            if area > m:
                m = area
    return m


w, h = map(int,input().split())
paper = [[0]*(w+1) for _ in range(h+1)]
cut_cnt = int(input())
w_idx = [0]
h_idx = [0]
for _ in range(cut_cnt):
    c, line = map(int,input().split())
    if c == 0:
        h_idx.append(line)
    else:
        w_idx.append(line)
h_idx.append(h)
w_idx.append(w)
w_list = sorted(w_idx)
h_list = sorted(h_idx)
print(max_area(w_list,h_list))

