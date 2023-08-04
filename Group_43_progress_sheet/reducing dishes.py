class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        prefix_sum = 0
        like_time_coefficient = 0
        for sat in satisfaction:
            prefix_sum += sat
            if prefix_sum < 0:
                break
                
            like_time_coefficient += prefix_sum

        return like_time_coefficient
