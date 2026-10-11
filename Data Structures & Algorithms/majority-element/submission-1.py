class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = {}
        for num in nums:
            if num not in count:
                count[num]=1
            else:
                count[num]+=1
        print(count)
        for i in count.keys():
            if count[i] > len(nums)/2:
                return i
        return -1