# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: TreeNode
        """
        # 두 트리를 하나로 합치기
        # 두 노드가 겹치는 경우 노드 값을 병합된 노드의 새 값으로 합침 
        # 그렇지 않으면 NOT null 노드가 새 트리의 노드로 사용됨