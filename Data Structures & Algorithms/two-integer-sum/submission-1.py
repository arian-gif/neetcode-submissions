class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {}
        
        for i in range(len(nums)):
            part2 = target-nums[i]
            if part2 in seen:
                return [seen[part2],i]
            seen[nums[i]] =i
        
        return -1