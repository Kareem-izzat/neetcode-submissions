# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        large=max(p.val,q.val)
        small=min(p.val,q.val)

        def dfs(root):
            if  large >=root.val and small<=root.val:
                return root
            if root.val < small:
                ans=dfs(root.right)
            if root.val > large:
                ans=dfs(root.left)
            return ans

        return dfs(root)