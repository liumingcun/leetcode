# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        ans = head
        while head != None:
            if head.next != None and head.next.val == head.val:
                head.next = head.next.next
            else:
                head = head.next
        return ans