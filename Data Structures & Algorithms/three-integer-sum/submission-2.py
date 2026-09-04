class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sol = []
        sorted_nums = sorted(nums)
        
        for i,num in enumerate(sorted_nums):
            if i >0 and sorted_nums[i] == sorted_nums[i-1]:
                continue 
            l,r = i+1, len(nums)-1
            target = 0-num

            while l<r:
                currSum = sorted_nums [r]+sorted_nums[l]
                if currSum>target:
                    r-=1
                elif currSum<target:
                    l+=1
                else:
                    sol.append([num,sorted_nums[l],sorted_nums[r]])
                    l+=1
                    r-=1
                    while l<r and sorted_nums[l]==sorted_nums[l-1]:
                        l+=1
                    while l<r and r<len(nums)-1 and sorted_nums[r]==sorted_nums[r+1]:
                        r+=1
        
        return sol


        