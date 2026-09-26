class Solution:
    def arrangeCoins(self, n: int) -> int:
        sum = 0
        res = 0
        if n == 1:
            return 1
        for i in range(1,n):
            if sum + i > n:
                break
            else:
                res+=1
            sum+=i
            
        
        return res