from collections import Counter 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c: dict = Counter(nums)

        for key in c.keys():
            if c[key]>1:
                return True

        return False 
        