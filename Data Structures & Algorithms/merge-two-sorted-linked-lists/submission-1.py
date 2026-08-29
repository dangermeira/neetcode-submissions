# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy & node are both ONE node object, node is used to build it and dummy maintains the head
        dummy = node = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1
                list1 = list1.next
            else:
                node.next = list2
                list2 = list2.next
            # once node.next is initialized, we have to move forward
            node = node.next

        # 'or' returns truthy values, None is falsy so the non-empty list is appended at the end
        node.next = list1 or list2

        return dummy.next

        