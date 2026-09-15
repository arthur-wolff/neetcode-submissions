class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        y = dict()
        for i in range(len(nums)):
            if nums[i] in y:
                return[y[nums[i]],i]
            x = target - nums[i]
            y[x] = i

        
            
            
            