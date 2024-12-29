"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not p or not q: 
            return None
        
        p_parents = deque()
        p_parents.append(p)
        while p.parent: 
            p_parents.appendleft(p.parent)
            p = p.parent
                
        q_parents = deque()
        q_parents.append(q)
        while q.parent: 
            q_parents.appendleft(q.parent)
            q = q.parent

        print([v.val for v in q_parents])
        print([v.val for v in p_parents])

        long = p_parents 
        short = q_parents
        if len(long) < len(short):
            long, short = short, long
        
        for i in range(len(long)-len(short)): 
            long.pop()
        
        
        while p_parents and q_parents: 
            if p_parents[-1] == q_parents[-1]: 
                return p_parents[-1]
            p_parents.pop()
            q_parents.pop()
        print(p_parents)
        print(q_parents)
        return None


