class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # find the point of rotation
        def b_search(l,r):
            while l<=r:
                m = (l+r)//2
                if nums[m]<target:
                    l=m+1
                elif nums[m]>target:
                    r = m-1
                else:
                    return m
            return -1
        
        # 2 lists and we find point of seperation
        l,r = 0, len(nums)-1
        if nums[r]>nums[l]:
            return b_search(l,r)
        found = False
        while l<=r and not found:
            m = (l+r)//2
            if nums[m]>=nums[l]:
                if nums[l]<=target<=nums[m]:
                    found = True
                    r = m
                else:
                    l=m+1

            elif nums[m]<nums[r]:
                if nums[m]<=target<=nums[r]:
                    found = True
                    l = m
                else:
                    r=m-1
        return b_search(l,r)
            




        