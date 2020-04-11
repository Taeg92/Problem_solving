# Problem [5110] : 수열 합치기

import sys
sys.stdin = open('input.txt')

class Node:

    def __init__(self, data):
        self.data = data
        self.link = None

class LinkedList:

    def __init__(self):
        new_node = Node('head')
        self.head = new_node
        self.tail = new_node
        self.before = None
        self.current = None
        self.num_of_data = 0

    def append(self, data):
        new_node = Node(data) 
        self.tail.link = new_node
        self.tail = new_node 
        self.num_of_data += 1

    def first(self):
        if self.num_of_data == 0:
            return None
        self.before = self.head
        self.current = self.head.link
        return self.current.data

    def next(self):
        self.before = self.current
        self.current = self.current.link
        if self.current == None:
            return None
        return self.current.data

    def insertlist(self, new_list):
        insert_num = new_list.first()
        num = self.first()
        
        for _ in range(self.num_of_data):
            if num > insert_num:
                self.before.link = new_list.head.link
                new_list.tail.link = self.current
                self.num_of_data += new_list.num_of_data
                break
            num = self.next()
        else: 
            self.tail.link = new_list.head.link
            self.num_of_data += new_list.num_of_data


    def result(self):
        lst = []
        num = self.first()
        for i in range(self.num_of_data):
            lst.append(num)
            num = self.next()
        return ' '.join(map(str, lst[-1:-11:-1]))

if __name__ == "__main__":
    T = int(input())
    for tc in range(1, T+1):
        N, M = map(int, input().split())

        l1 = LinkedList()
        for i in map(int, input().split()):
            l1.append(i)

        for _ in range(M - 1):
            l2 = LinkedList()
            for j in map(int, input().split()):
                l2.append(j)
            l1.insertlist(l2)
        
        print('#{} {}'.format(tc, l1.result()))