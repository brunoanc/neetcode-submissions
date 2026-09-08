from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        q = deque([(root, 0)])
        node_list = []

        while q:
            node, level = q.popleft()

            if len(node_list) <= level:
                node_list.append([node.val])
            else:
                node_list[level].append(node.val)

            if node.left is not None:
                q.append((node.left, level + 1))

            if node.right is not None:
                q.append((node.right, level + 1))

        return node_list