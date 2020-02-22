# Problem [1224] : 계산기

import sys
sys.stdin = open('input.txt')


if __name__ == "__main__":
    T = 10
    for tc in range(1, T+1):
        N = input()
        D = input()
        calc = list()
        stack = list()
        R = list()
        for c in D:
            if c.isdigit():
                calc.append(c)
            elif c == ')':
                while stack[-1] != '(':
                    calc.append(stack.pop())
                stack.pop()
            else:
                if c == '+':
                    if stack[-1]=='*':
                        while stack[-1] != '(' and stack[-1] != '+':
                            calc.append(stack.pop())
                stack.append(c)
        for c in calc:
            if c == '+':
                R.append(R.pop()+R.pop())
            elif c == '*':
                R.append(R.pop()*R.pop())
            else:
                R.append(int(c))
        print('#{} {}'.format(tc,R[0]))