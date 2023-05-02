# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def _BFS(node1,node2):
            if node1 is None and node2 is None:
                return True
            elif node1 is None and node2 is not None or node2 is None and node1 is not None:
                return False
            if node1.val != node2.val:
                return False

            return _BFS(node1.left, node2.left) and _BFS(node1.right,node2.right)

        return _BFS(p,q)
