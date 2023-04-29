# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def _DFS(node, level):
            if node is None: return level
            return max(_DFS(node.left, level+1),_DFS(node.right, level+1))
        return _DFS(root,0)
