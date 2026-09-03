class Solution:
    def climbStairs(self, n: int) -> int:
        #step 5
        #  5
        # 
        mem = {}
        def stairs(step):
            if step in mem:
                return mem[step]
            if step==n:
                return 1
            elif step > n:
                return 0
            else:
                mem[step]= stairs(step+1)+stairs(step+2)
            return mem[step]
        return stairs(0)
        