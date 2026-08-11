class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}

        for i in range(len(nums)):
            curr = nums[i]
            two = target-nums[i]
            if two in pairs:
                return [pairs[two],i]
            pairs[curr]= i
        return []

        