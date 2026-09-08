# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path = {root.val}
        curr = root

        while curr.val != p.val:
            if p.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

            path.add(curr.val)

        curr = root
        coincidences = [root]

        while curr.val != q.val:
            if q.val > curr.val:
                curr = curr.right
            else:
                curr = curr.left

            if curr.val in path:
                coincidences.append(curr)

        return coincidences[-1]