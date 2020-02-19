# Problem [14889] : 스타트와 링크

from itertools import combinations as combi
import sys
sys.stdin = open('input.txt')

if __name__ == '__main__':

    N = int(input())
    d = [list(map(int,input().split())) for _ in range(N)]
    m = 100000000
    team = list(combi(range(N),N//2))

    for home_team in team:
        away_team = list()
        for n in range(N):
            if n not in home_team:
                away_team.append(n)
        sum_home = 0
        for i in range(N//2):
            for j in range(i+1,N//2):
                sum_home += d[home_team[i]][home_team[j]] + d[home_team[j]][home_team[i]]
        sum_away =0
        for i in range(N//2):
            for j in range(i+1,N//2):
                sum_away += d[away_team[i]][away_team[j]] + d[away_team[j]][away_team[i]]
        m = min(m,abs(sum_away-sum_home))
    print(m)