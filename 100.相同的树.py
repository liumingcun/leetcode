# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 深度优先搜索 先序遍历
class Solution:

    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        ans1 = []
        ans2 = []
        self.search(p, ans1)
        self.search(q, ans2)
        if ans1 == ans2:
            return True

    def search(self, p: TreeNode, ans):
        if p == None:
            ans.append('null')
            return
        ans.append(p.val)
        self.search(p.left, ans)
        self.search(p.right, ans)









