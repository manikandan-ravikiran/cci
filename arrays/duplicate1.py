class Solution:
    def singleNumber(self, ar: List[int]) -> int:
        
        res = ar[0] 
      
        for i in range(1,len(ar)): 
            res = res ^ ar[i] 

        return res