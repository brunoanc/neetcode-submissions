# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node

        return prev

    def reorderList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if fast is None:
                break

        first_half = head

        slow_next = slow.next
        slow.next = None
        second_half = self.reverseList(slow_next)

        while first_half and second_half:
            f_h_next = first_half.next
            s_h_next = second_half.next
            first_half.next = second_half
            second_half.next = f_h_next
            first_half = f_h_next
            second_half = s_h_next
