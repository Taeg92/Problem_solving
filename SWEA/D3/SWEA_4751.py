# Problem [4751] : 다솔이의 다이아몬드 장식

T = int(input())

for tc in range(T):
    word = input()
    size = len(word)
    x = '..#.'
    y = '.#'
    w_line = ''
    for char in word:
        w_line += ('#.' + char + '.')
    print(x*size + '.')
    print(y*(2*size) + '.')
    print(w_line + '#')
    print(y*2*size+'.')
    print(x*size+'.')