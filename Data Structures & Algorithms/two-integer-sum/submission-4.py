class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = set(nums)
        for i,_ in enumerate(nums):
            b = target - nums[i]
            if   b in s and b in nums[i+1:]:
                return [i, nums.index(b, i+1)]
            

        