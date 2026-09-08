# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def in_order_traversal(self, curr: Optional[TreeNode], k: int) -> int:
        if curr.left is not None:
            v = self.in_order_traversal(curr.left, k)

            if v != 0:
                return v

        self.i += 1

        if self.i == k:
            return curr.val

        if curr.right is not None:
            v = self.in_order_traversal(curr.right, k)

            if v != 0:
                return v

        return 0

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.i = 0
        return self.in_order_traversal(root, k)
