class Solution:
    def max_steps(self, A):
        
        dp=[0]*(A+1)
        dp[0]=1
        dp[1]=1
        for i in range(2,A+1):
            dp[i]=dp[i-1]+dp[i-2]
            
        return dp[A]%1000000007
        
