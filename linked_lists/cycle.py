# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head is None: return False
        fast, slow = head, head
        while True:
            for _ in range(2):
                if fast.next is None: return False
                else:
                    fast = fast.next
            slow = slow.next
            if slow == fast:
                return True
