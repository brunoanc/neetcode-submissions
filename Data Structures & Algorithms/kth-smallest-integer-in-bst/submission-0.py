# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    i = 0

    def in_order_traversal(self, curr: Optional[TreeNode], k: int) -> int:
        r = 0

        if curr.left is not None:
            r += self.in_order_traversal(curr.left, k)

        self.i += 1

        if self.i == k:
            return curr.val

        if curr.right is not None:
            r += self.in_order_traversal(curr.right, k)

        return r

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        return self.in_order_traversal(root, k)
