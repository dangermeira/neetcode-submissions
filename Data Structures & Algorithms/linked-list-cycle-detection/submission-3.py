# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr1 = head
        curr2 = head

        while curr1 is not None and curr2 is not None and curr2.next is not None:
            curr2 = curr2.next.next
            curr1 = curr1.next
            if curr2 == curr1:
                return True
        return False
        