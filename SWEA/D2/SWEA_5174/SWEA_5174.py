# Problem [5174] : subtree

import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data
        
class Tree:
    def __init__(self, cnt):
        self.node_lst = [None]
        for i in range(E + 1):
            self.node_lst.append(Node(i))
        
    def put(self, parent, child):
        if self.node_lst[parent].left == None:
            self.node_lst[parent].left = self.node_lst[child]
        else:
            self.node_lst[parent].right = self.node_lst[child]
            
    def count(self, node):
        self.cnt += 1
        if node.left != None:
            self.count(node.left)
        if node.right != None:
            self.count(node.right)
        
    
    def result(self, num):
        self.cnt = 0
        self.count(self.node_lst[num])
        return self.cnt

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        E, N = map(int, input().split())
        D = list(map(int, input().split()))
        t = Tree(E)
        for i in range(E):
            t.put(D[i*2], D[i*2 + 1])
        print('#{} {}'.format(tc, t.result(N)))