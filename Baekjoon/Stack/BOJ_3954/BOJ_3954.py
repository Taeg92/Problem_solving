# Problem [3954] : Brainf**k 인터프리터

import sys
sys.stdin = open('input.txt')

def search_pair(arr):
    temp = list()
    for i in range(len(arr)):
        if arr[i] == '[':
            temp.append(i)
        elif arr[i] == ']':
            idx = temp.pop()
            Pair[idx] = i
            Pair[i] = idx

def BF_Prog(Program,Input):
    stack = list()
    cnt = 0
    memory = [0] * Sm
    pos = 0
    i_pos = 0
    m_pos = 0
    while cnt < 50000000:
        if pos >= Sc:
            break
        if Program[pos] == '-':
            memory[m_pos] = (memory[m_pos] - 1) % 256
            pos += 1
        elif Program[pos] == '+':
            memory[m_pos] = (memory[m_pos] + 1) % 256
            pos += 1
        elif Program[pos] == '<':
            m_pos = (m_pos - 1) % Sm
            pos += 1
        elif Program[pos] == '>':
            m_pos = (m_pos + 1) % Sm
            pos += 1
        elif Program[pos] == '[':
            if memory[m_pos] == 0:
                pos = Pair[pos]
                pos += 1
            else:
                stack.append(pos)
                pos += 1
        elif Program[pos] == ']':
            if memory[m_pos] != 0:
                pos = Pair[pos]
                pos += 1
            else:
                stack.pop()
                pos += 1
        elif Program[pos] == '.':
            pos += 1
        else:
            memory[m_pos] = Input[i_pos]
            if i_pos < Si:
                i_pos += 1
            pos += 1
        cnt += 1
    
    if cnt == 50000000:
        return f'Loops {stack[0]} {Pair[stack[0]]}'
    return f'Terminates'

if __name__ == "__main__":
    T= int(input())
    for tc in range(1, T+1):
        Sm, Sc, Si = map(int,input().split())
        P= list(input())
        I = list(map(ord,input())) + [255]
        Pair = dict()
        search_pair(P)
        print(BF_Prog(P,I))