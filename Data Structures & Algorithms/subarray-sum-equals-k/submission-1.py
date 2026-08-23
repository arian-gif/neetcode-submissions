class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # hash map prefixsum: count 
        sub_array = {
            0:1
        }

        curr, res= 0,0

        for n in nums:
            curr +=n
            res += sub_array.get(curr - k, 0)
            sub_array[curr] = sub_array.get(curr,0)+1 
        return res
        
        
        