from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        queue = deque() #(node, level)
        queue.append((root, 0))
        counts = []
        averages = []

        while len(queue) > 0:
            node, level = queue.popleft()
            if node is None: continue
            if level == len(averages):
                averages.append(node.val)
                counts.append(1)
            else:
                averages[level] = (averages[level] * counts[level] + node.val) / (counts[level] + 1)
                counts[level] += 1
            queue.append((node.left, level + 1))
            queue.append((node.right, level + 1))
        return averages
