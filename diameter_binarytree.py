# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def height(self,root):
        if root is None:
            return 0
        LeftHeight=self.height(root.left)
        RightHeight=self.height(root.right)
        return max(LeftHeight,RightHeight)+1
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        LeftHeight=self.height(root.left)
        RightHeight=self.height(root.right)

        currentdiameter=LeftHeight+RightHeight

        LeftHeight=self.diameterOfBinaryTree(root.left)
        RightHeight=self.diameterOfBinaryTree(root.right)
        
        return max(LeftHeight,RightHeight,currentdiameter)
        