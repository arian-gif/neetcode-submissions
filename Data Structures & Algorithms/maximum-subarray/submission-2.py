class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr = nums[0]

        for num in nums[1:]:
            curr = max(num,curr+num)
            max_sum=max(curr,max_sum)
        return max_sum
        