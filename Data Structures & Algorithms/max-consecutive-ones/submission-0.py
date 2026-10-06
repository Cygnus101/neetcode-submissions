class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_ones = 0
        ones = 0
        for i in nums: 
            if i== 1:
                ones+=1
            else:
                if ones>max_ones:
                    max_ones = ones
                ones = 0
        if ones>max_ones:
            return ones
        return max_ones