# bottom up approach
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s) + 1)
        dp[-1] = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == '0':
                continue
            else:
                dp[i] += dp[i+1]
            
            if i < len(s) - 1 and int(s[i:i+2]) < 27:
                dp[i] += dp[i+2]
            
        return dp[0]
      
      
      
# top-down approach
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(index):
            if index >= len(s):
                return 1
            
            if s[index] == '0':
                return 0

            count = dp(index + 1)
            if index + 1 < len(s) and int(s[index] + s[index + 1]) < 27:
                count += dp(index + 2)
            
            return count
        
        return dp(0)
