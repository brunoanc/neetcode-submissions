# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        head = curr

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                curr = curr.next
                list1 = list1.next
            else:
                curr.next = list2
                curr = curr.next
                list2 = list2.next

        if list1:
            curr.next = list1
        elif list2:
            curr.next = list2

        return head.next
 
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            new_lists = []

            for i in range(0, len(lists), 2):
                if i + 1 >= len(lists):
                    new_lists.append(lists[i])
                else:
                    new_lists.append(self.mergeTwoLists(lists[i], lists[i + 1]))

            lists = new_lists

        return lists[0]