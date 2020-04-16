# Problem [5178] : 노드의 합

import sys
sys.stdin = open('input.txt')

class Tree:
    def __init__(self, N):
        self.lst = [0] * (N + 1)
        self.N = N

    def put(self, num1, num2):
        self.lst[num1] = num2
    
    def search_leaf(self, node):
        if node * 2 > N: 
            self.sum += self.lst[node] 
        else: 
            self.search_leaf(node * 2) 
            if node * 2 != N: 
                self.search_leaf(node * 2 + 1) 
    
    def result(self, L):
        self.sum = 0
        self.search_leaf(L)
        return self.sum

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M, L = map(int, input().split())
        t = Tree(N)
        for _ in range(M):
            n1, n2 = map(int, input().split())
            t.put(n1, n2)
        print('#{} {}'.format(tc, t.result(L)))