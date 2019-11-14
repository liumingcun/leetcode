# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = ListNode(None)
        ans = l3
        while l1 and l2:
            if l1.val < l2.val:
                ans.next, l1 = l1, l1.next
            else:
                ans.next, l2 = l2, l2.next
            ans = ans.next
        if l1:
            ans.next = l1
        else:
            ans.next = l2
        return l3.next