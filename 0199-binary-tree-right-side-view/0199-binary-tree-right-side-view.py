from collections import deque
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        if root is None:
            return []
        #Solution 1
        # queue = deque([root])
        # result = []
        # last_node = None
        # while queue:
        #     levels= len(queue)
        #     #keep popleft until the farright node become last node
        #     for level in range(levels):
        #         current_node = queue.popleft()
        #         last_node = current_node.val
        #         if current_node.left:
        #             queue.append(current_node.left)
        #         if current_node.right:
        #             queue.append(current_node.right)
        #     result.append(last_node)
        # return result
        #-------------
        #Solution 2, optimize to not calculate len(queue) inside the loop
        
        queue = deque([(root,0)])
        result = []
        while queue:
            current,level = queue.popleft()
            if level == len(result):
                if not queue:
                    result.append(current.val)
                elif queue[0][1] != level:
                    result.append(current.val)
            if current.left:
                queue.append((current.left,level+1))
            if current.right:
                queue.append((current.right,level+1))

        return result