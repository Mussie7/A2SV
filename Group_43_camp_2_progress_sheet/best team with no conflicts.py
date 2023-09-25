class Solution:
    # top down approach
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        def dp(index, score_limit):
            if index == n:
                return 0

            if score_limit == -1:
                score_limit_value = 0
            else:
                score_limit_value = age_score[score_limit][1]
            
            if memo[index][score_limit] is not None:
                return memo[index][score_limit]

            # check whether the current index is eligible to be on the current team
            if age_score[index][1] >= score_limit_value:
                # compute whether adding the current index to the team is best or not
                memo[index][score_limit] = max(dp(index + 1, index) + age_score[index][1], dp(index + 1, score_limit))
                return memo[index][score_limit]
            else:
                memo[index][score_limit] = dp(index + 1, score_limit)
                return memo[index][score_limit]


        n = len(ages)
        age_score = [(ages[i], scores[i]) for i in range(n)]
        age_score.sort()
        # @cache and dictionary memoization doesn't work because leetcode keeps giving MLE
        memo = [[None for _ in range(n+1)] for _ in range(n)]
        return dp(0, -1)

    # bottom-up approach
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        n = len(ages)
        age_score = [(scores[i], ages[i]) for i in range(n)]
        # sort the array by the age and score in that order
        age_score.sort(key=lambda x: (x[1], x[0]))

        dp = [age_score[i][0] for i in range(n)]
        for i in range(n - 1, -1, -1):
            for j in range(i+1, n):
                # for every index choose the best next eligible player
                if age_score[i] <= age_score[j]:
                    dp[i] = max(dp[i], dp[j] + age_score[i][0])
        
        return max(dp)
