# Problem [17281] : 야구

from itertools import permutations
import sys
sys.stdin = open('input.txt')

m = -sys.maxsize

if __name__ == "__main__":
    N = int(input())
    D = [list(map(int,input().split())) for _ in range(N)]
    
    for permutation in permutations(range(1,9)):
        order = list(permutation)[:3] + [0] + list(permutation)[3:]
        start = 0
        score = 0
        for n_inning in D:
            base1, base2, base3 = 0, 0, 0
            out = 0
            while 1:
                if out >= 3:
                    break
                player = n_inning[order[start]]
                if player == 0:
                    out += 1        
                elif player == 1:
                    score += base3
                    base1, base2, base3 = 1, base1, base2
                elif player == 2:
                    score += base2 + base3
                    base1, base2, base3 = 0, 1, base1
                elif player == 3:
                    score += base1 + base2 + base3
                    base1, base2, base3 = 0, 0, 1 
                else:
                    score += base1 + base2 + base3 + 1
                    base1, base2, base3 = 0, 0, 0
                
                start = (start + 1) % 9
        m = max(m,score)
    print(m)