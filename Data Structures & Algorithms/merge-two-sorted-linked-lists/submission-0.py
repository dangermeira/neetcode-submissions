# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = ListNode()
        newListHead = newList
        l1 = list1
        l2 = list2

        while l1 or l2:
            if l1 == None:
                newList.next = l2
                newList = newList.next
                l2 = l2.next
            elif l2 == None:
                newList.next = l1
                newList = newList.next
                l1 = l1.next
            elif l1.val <= l2.val:
                newList.next = l1
                newList = newList.next
                l1 = l1.next
            elif l2.val <= l1.val:
                newList.next = l2
                newList = newList.next
                l2 = l2.next
        return newListHead.next