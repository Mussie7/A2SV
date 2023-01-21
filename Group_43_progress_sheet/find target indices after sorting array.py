class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        counter_array = [0] * (max(nums) + 1)
        if target > len(counter_array)-1:
            return

        for num in nums:
            counter_array[num] += 1

        start = sum(counter_array[:target])
        return [i for i in range(start, start+counter_array[target])]
