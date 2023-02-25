class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sum_dic = Counter([0])
        prefix_sum = subarrays = 0
        
        for num in nums:
            prefix_sum += num
            if prefix_sum - k in sum_dic:
                subarrays += sum_dic[prefix_sum - k]

            sum_dic[prefix_sum] += 1
        
        return subarrays
