# problem [5122] : 수열 편집

import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():

    length = 0

    def __init__(self, head = None):
        self.head = head
        self.next = None
    
    def append(self, item):
        current = self.head
        if not self.head:
            self.head = item
        else:
            while current.next:
                current = current.next
            current.next = item
        self.length += 1
    
    def show(self):
        current = self.head
        result = list()
        if not self.head:
            result.append('None')
        else:
            while current.next:
                result.append(str(current.value))
                current = current.next
            result.append(str(current.value))
        return print(' '.join(result))
    
    def insert(self, idx, item):
        current = self.head
        for i in range(idx-1):
            current = current.next
        item.next = current.next
        current.next = item
        self.length += 1
            
    def delete(self, idx):
        data = int(self.getData(idx))
        if self.head.value == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.value != data:
                temp = temp.next
            temp.next = temp.next.next
        self.length -= 1
    
    def getData(self, idx):
        if idx == 0:
            return f'{self.head.value}'
        else:
            cur = self.head
            for _ in range(idx):
                cur = cur.next
            return f'{cur.value}'
    
    def change(self, idx, item):
        if idx == 0:
            self.head.value = item
        else:
            cur = self.head
            for _ in range(idx):
                cur = cur.next
            cur.value = item

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    l = LinkedList()
    for i in map(int, input().split()):
        l.append(Node(i))
    for _ in range(M):
        D = list(input().split())
        if D[0] == 'I':
            l.insert(int(D[1]), Node(int(D[2])))
        elif D[0] == 'D':
            l.delete(int(D[1]))
        elif D[0] == 'C':
            l.change(int(D[1]), int(D[2]))
    result = 0
    if l.length < L:
        result = -1
    else:
        result = l.getData(L)
    print('#{} {}'.format(tc, result))
