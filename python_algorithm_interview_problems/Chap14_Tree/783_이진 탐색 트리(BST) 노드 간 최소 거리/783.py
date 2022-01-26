# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # Binary Search Tree (BST)
        # 두 노드가 가진 값의 차이 최솟 값 출력
        
        # 연결리스트니까 주어진 값 중에 최솟값 2개 뽑아서 차이 구하는 방법은 안된다
        # 노드 탐색하면서 val값이 min인 것 따로 저장해둔다 (min1, min2 이렇게 2개)
        # 아니지 val가 작은게 문제가 아니라, 49-48이어도 차이가 1인 것을 찾을 줄도 알아야하네.
        # null은 pass
        
        # DFS로 비교. 4고정 4-2, 4-1, 4-3 => 4-6 (음수는 pass)
        # 대박,, BST의 특징 -> 자기 자식의 왼쪽노드는 무조건 자기보다 작음 ;; 깜빡했음 ㅋㅋ
        # 그럼 생각 해보쟈구
        # (현재 루트 노드 - 왼쪽 자식 노드) 의 val을 구해서 temp에 저장해두고
        # 오른쪽으로 갈 때는 (오른쪽 자식 노드 - 현재 루트 노드) 구해서 res = min(temp, 계산값) 해서 출력하면 될 듯 천재냐?
        