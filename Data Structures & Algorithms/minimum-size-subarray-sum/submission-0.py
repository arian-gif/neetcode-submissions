class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums)<target:
            return 0
        l,curr,best = -1,0,len(nums)
        for r in range(len(nums)):
            curr +=nums[r]
            while curr >= target:
                best = min(best, r-l)
                l+=1
                curr-=nums[l]
        return best
        