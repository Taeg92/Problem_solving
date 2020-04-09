# Problem [5108] : 숫자 추가

import sys
sys.stdin = open('input.txt')

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList():

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
    
    
    def insert(self, item, position):
        current = self.head
        for i in range(position-1):
            current = current.next
        item.next = current.next
        current.next = item
        
            
    def delete(self, data):
        if self.head.value == data:
            self.head = self.head.next
        else:
            temp = self.head
            while temp.next.value != data:
                temp = temp.next
            temp.next = temp.next.next
    
    def getData(self, idx):
        if idx == 0:
            return f'{self.head.value}'
        else:
            cur = self.head
            for i in range(idx):
                cur = cur.next
            return f'{cur.value}'



T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    D = list(map(int,input().split()))
    l = LinkedList()
    for i in range(N):
        l.append(Node(D[i]))
    for _ in range(M):
        idx, *items = map(int, input().split())
        for item in items:
            l.insert(Node(item), idx)
    
    print('#{} {}'.format(tc, l.getData(L)))