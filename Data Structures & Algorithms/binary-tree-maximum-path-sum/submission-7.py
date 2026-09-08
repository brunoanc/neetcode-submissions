# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_path(self, curr: Optional[TreeNode]) -> int:
        left_sum = 0
        right_sum = 0

        if curr.left is not None:
            left_sum = self.max_path(curr.left)

        if curr.right is not None:
            right_sum = self.max_path(curr.right)

        s = curr.val

        if left_sum > 0:
            s += left_sum

        if right_sum > 0:
            s += right_sum

        if s > self.max_sum:
            self.max_sum = s

        return curr.val + max(left_sum, right_sum, 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        return max(self.max_path(root), self.max_sum)
