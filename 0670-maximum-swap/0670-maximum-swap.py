class Solution:
    def maximumSwap(self, num: int) -> int:
        num_list = list(str(num))
        n = len(num_list)
        if n == 1: 
            return num
        maximum = num
        for i in range(n):
            for j in range(i+1, n): 
                num_list[i], num_list[j] = num_list[j], num_list[i]
                maximum  = max(int(''.join(num_list)), maximum)
                num_list[i], num_list[j] = num_list[j], num_list[i]
        return maximum

            
            