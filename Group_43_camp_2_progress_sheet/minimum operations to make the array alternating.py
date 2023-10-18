class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def findSecondMax(counter, max_val):
            max_num = 0
            max_count = 0
            for num in counter:
                if num != max_val and counter[num] > max_count:
                    max_count = counter[num]
                    max_num = num
            
            return max_num, max_count

        n = len(nums)
        odd = Counter()
        even = Counter()
        max_odd, max_even = 0, 0
        max_odd_count, max_even_count = 0, 0
        for i in range(n):
            if i % 2 == 1:
                odd[nums[i]] += 1
                if odd[nums[i]] > max_odd_count:
                    max_odd_count = odd[nums[i]]
                    max_odd = nums[i]
            else:
                even[nums[i]] += 1
                if even[nums[i]] > max_even_count:
                    max_even_count = even[nums[i]]
                    max_even = nums[i]
        
        if max_odd == max_even:
            # if there is only one element in one of the counters find the second maximum from the other counter
            # p.s. if there is only one element in both counters the func returns 0 as the count so it'll be fine in the final calculation
            # p.s. 0 means all the elements must change
            if len(even) == 1 and len(odd) > 1:
                max_odd, max_odd_count = findSecondMax(odd, max_odd)
            elif len(odd) == 1 and len(even) > 1:
                max_even, max_even_count = findSecondMax(even, max_even)
            else:
                # decide the best alternative of choosing the second maximum from either counters
                second_max_odd, second_max_odd_count = findSecondMax(odd, max_odd)
                second_max_even, second_max_even_count = findSecondMax(even, max_even)
                return min((math.ceil(n / 2) - max_even_count) + (n // 2 - second_max_odd_count),
                            (math.ceil(n / 2) - second_max_even_count) + (n // 2 - max_odd_count)) 

        # calculate the operations to change the numbers to the most common number in the counters
        return (math.ceil(n / 2) - max_even_count) + ((n // 2) - max_odd_count)
