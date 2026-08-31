class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tar = {}

        for i, num in enumerate(nums):
            print(i,num)
            want = target - num

            if want in tar:
                return [tar[want],i]
            tar[num] = i
        
        return []
            
