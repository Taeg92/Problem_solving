# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head and head.val == val:
            head = head.next
        if not head:
            return head

        next_node = head
        while next_node and next_node.next:
            if next_node.next.val == val:
                next_node.next = next_node.next.next
            else:
                next_node = next_node.next

        return head
