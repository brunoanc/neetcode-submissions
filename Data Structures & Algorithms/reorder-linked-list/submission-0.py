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
        length = 0
        curr = head

        while curr:
            curr = curr.next
            length += 1

        first_half = head
        second_half = head
        first_half_len = length // 2 + length % 2

        for i in range(first_half_len):
            if i == first_half_len - 1:
                prev = second_half
                second_half = second_half.next
                prev.next = None
                continue

            second_half = second_half.next

        second_half = self.reverseList(second_half)

        while first_half and second_half:
            f_h_next = first_half.next
            s_h_next = second_half.next
            first_half.next = second_half
            second_half.next = f_h_next
            first_half = f_h_next
            second_half = s_h_next
