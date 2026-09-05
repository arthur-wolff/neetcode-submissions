class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        res = set()

        for i in nums:
            res.add(i)
        
        if len(res) < len(nums):
            return True
        else:
            return False
        

        