from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left is None and root.right is None: return True
        queue = deque([root.left, root.right])
        while len(queue) > 0:
            left, right  = queue.popleft(), queue.popleft()
            if left is None or right is None:
                if left != right: return False
                else: continue

            # print(queue, left.val, right.val)
            if left.val != right.val: return False

            for node in [left.left,right.right,left.right,right.left]:
                queue.append(node)
        return True
