class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)
        mid = high//2

        while low < high:
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid
                
            elif nums[mid] < target:
                low = mid + 1
            mid = (high+low)//2

        return -1