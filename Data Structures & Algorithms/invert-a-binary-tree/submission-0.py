# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # check that the root is a valid node
        if not root:
            return None

        # need to swap them simulteanously by having it on one line
        root.left, root.right = root.right, root.left
        
        # check recursively by calling the function on itself
        self.invertTree(root.left)
        self.invertTree(root.right)

        return root