# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def max_path(self, curr: Optional[TreeNode]) -> int:
        if curr.left is None and curr.right is None:
            return curr.val

        left_sum = float("-inf")
        right_sum = float("-inf")

        if curr.left is not None:
            left_sum = self.max_path(curr.left)

        if curr.right is not None:
            right_sum = self.max_path(curr.right)

        if curr.val < 0:
            if left_sum > self.max_sum:
                self.max_sum = left_sum

            if right_sum > self.max_sum:
                self.max_sum = right_sum
        else:
            if curr.val + left_sum + right_sum > self.max_sum:
                self.max_sum = curr.val + left_sum + right_sum

        return curr.val + max(left_sum, right_sum, 0)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_sum = float("-inf")
        return max(self.max_path(root), self.max_sum)
