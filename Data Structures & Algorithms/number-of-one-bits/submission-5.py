class Solution:
    def hammingWeight(self, n: int) -> int:
        ex = 0
        count = 0

        while n >= (2**ex):
            ex+=1
        ex-=1
        


        while n>0 and ex>=0:
            print(n,ex)
            if n>=2**ex:
                n -= 2**ex
                count+=1
            ex-=1
        return count

            

        


        
        