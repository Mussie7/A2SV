class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        n = len(quality)
        proportion = []
        for i in range(n):
            proportion.append([quality[i], wage[i]/quality[i]])
        
        proportion.sort(key=lambda x: x[1], reverse=True)
        ind_arr = list(range(n))
        ind_arr.sort(key=lambda x: proportion[x][0])

        sum_set = set(ind_arr[:k])
        quality_sum = 0
        for i in range(k):
            quality_sum += proportion[ind_arr[i]][0]
        sum_index = k
        
        paid_group_cost = inf
        for i in range(n - k + 1):
            while len(sum_set) < k:
                if ind_arr[sum_index] >= i:
                    sum_set.add(ind_arr[sum_index])
                    quality_sum += proportion[ind_arr[sum_index]][0]
                sum_index += 1
            
            paid_group_cost = min(paid_group_cost, quality_sum * proportion[i][1])
            if i in sum_set:
                sum_set.remove(i)
                quality_sum -= proportion[i][0]

        return paid_group_cost