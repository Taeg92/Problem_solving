from collections import defaultdict


def solution(n, results):

    def init_table(results):
        win_team = defaultdict(set)
        lose_team = defaultdict(set)

        for win, lose in results:
            win_team[win].add(lose)
            lose_team[lose].add(win)

        return win_team, lose_team

    def update_result(win_team, lose_team, n):
        for i in range(1, n + 1):
            for lose in win_team[i]:
                lose_team[lose] |= lose_team[i]
            for win in lose_team[i]:
                win_team[win] |= win_team[i]

    def get_valid_ranker(win_team, lose_team, n):
        cnt = 0
        for i in range(1, n + 1):
            if len(win_team[i]) + len(lose_team[i]) == n - 1:
                cnt += 1

        return cnt

    win_team, lose_team = init_table(results)

    update_result(win_team, lose_team, n)

    return get_valid_ranker(win_team, lose_team, n)


n = 5
results = [
    [4, 3], [4, 2],
    [3, 2], [1, 2],
    [2, 5]
]

print(solution(n, results))
