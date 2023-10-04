class Solution:
    def maxScore(self, nums: List[int]) -> int:
        @cache
        def dp(index_list):
            if len(index_list) == 0:
                return 0

            score = 0
            operation = (len(nums) // 2) - (len(index_list) // 2) + 1
            index_set = set(index_list)
            for i in range(len(index_list)):
                index_set.remove(index_list[i])
                for j in range(i + 1, len(index_list)):
                    index_set.remove(index_list[j])
                    score = max(score, 
                    (gcd(nums[index_list[i]], nums[index_list[j]]) * operation) + dp(tuple(sorted(index_set))))
                    
                    index_set.add(index_list[j])
                
                index_set.add(index_list[i])
            
            return score
        

        index_list = tuple([i for i in range(len(nums))])
        return dp(index_list)
