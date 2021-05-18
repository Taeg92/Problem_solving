def solution(absolutes, signs):
    return sum([absolutes[i] if signs[i] == True else absolutes[i] * (-1) for i in range(len(absolutes))])

absolutes = [4, 7, 12]
signs = [True, False, True]

print(solution(absolutes, signs))