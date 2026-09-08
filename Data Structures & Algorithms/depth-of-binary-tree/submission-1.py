# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_depth(self, curr: Optional[TreeNode]):
        if curr is None:
            return 0

        return 1 + max(self.dfs_depth(curr.left), self.dfs_depth(curr.right))

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.dfs_depth(root)
