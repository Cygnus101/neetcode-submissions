class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        min_score = math.inf
        L = 0
        R = k
        
        while R <= len(nums):
            window = nums[L:R]
            score = window[-1] - window[0]
            if score < min_score:
                min_score= score
            L+=1
            R+=1

        return min_score        



