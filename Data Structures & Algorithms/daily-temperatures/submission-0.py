class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        sol = [0]*len(temperatures)

        for i,temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                _,j = stack.pop()
                days = i-j
                sol[j]=days
            stack.append((temp,i))
        return sol
        