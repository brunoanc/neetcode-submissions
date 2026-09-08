# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def dfs_equal(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None or q is None:
            return p == q

        if p.val != q.val:
            return False

        return self.dfs_equal(p.left, q.left) and self.dfs_equal(p.right, q.right)

    def dfs_check_subtree(self, curr: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if curr is None:
            return False

        if self.dfs_equal(curr, subRoot):
            return True

        return self.dfs_check_subtree(curr.left, subRoot) or self.dfs_check_subtree(curr.right, subRoot)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        return self.dfs_check_subtree(root, subRoot)