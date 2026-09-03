class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findBound(left):
            l,r = 0, len(nums)-1
            result = -1
            while l<=r:
                m = (l+r)//2
                if nums[m]<target:
                    l=m+1
                elif nums[m]>target:
                    r=m-1
                else:
                    result = m 
                    if left:
                        r= m-1
                    else:
                        l=m+1
            return result
        left = findBound(True)
        if left ==-1:
            return [-1,-1]
        right = findBound(False)
        return [left,right]