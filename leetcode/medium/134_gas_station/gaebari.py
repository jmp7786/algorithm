# https://leetcode.com/problems/gas-station
# Runtime: 3112 ms, faster than 11.89% of Python online submissions for Gas Station.
# Memory Usage: 13.6 MB, less than 9.09% of Python online submissions for Gas Station.

class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        for i in range(len(gas)):
            tank = 0
            for j in range(i, len(gas) + i):
                if j >= len(gas):
                    j = j-len(gas)
                tank += gas[j]
                tank -= cost[j]
                if tank < 0:
                    break
            if tank >= 0:
                return i
        return -1
