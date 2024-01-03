# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        #using inorder DFS so [2,1,3] will be tranversed as [1,2,3]
        def inorder_dfs(node):
            if not node:
                return []
            return inorder_dfs(node.left) + [node.val] + inorder_dfs(node.right)
        checking_list  = inorder_dfs(root)
        for i in range(len(checking_list)-1):
            if checking_list[i]>=checking_list[i+1]:
                return False
        return True
            
        
            
        