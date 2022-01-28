# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # 두 노드 간 가장 긴 경로의 길이를 출력
        # 가장 긴 경로 찾으려면 - 1. 가장 말단(리프 노드)까지 탐색한 다음 부모로 거슬러 올라간다
        #                    2. 거슬러 올라가며 각각의 거리를 계산해 상태값을 업데이트하면서 누적해간다
        