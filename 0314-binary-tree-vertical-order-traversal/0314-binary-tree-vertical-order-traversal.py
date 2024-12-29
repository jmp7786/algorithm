# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: 
            return []
        memo = defaultdict(list)
        def traversal(node, label, level, direction, memo): 
            lst = memo[label]
            lst.append((node.val, level, direction))
            if node.left: 
                traversal(node.left, label-1, level+1, 1, memo)
            if node.right: 
                traversal(node.right, label+1, level+1, 0, memo)
        
        traversal(root, 0, 0, 0, memo)
        keys = sorted(memo.keys())
        result = []
        for k in keys: 
            # print(memo[k],0)
            curr = sorted(memo[k], key = lambda x: (x[1]))
            # print(curr,1)
            result.append([v[0] for v in curr])
            # print()

        return result
