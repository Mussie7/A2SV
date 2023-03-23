class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        offset = min(nums)
        rnge = max(nums) - offset + 2
        counter = [0] * rnge

        for num in nums:
            counter[num-offset] += 1
        
        cnt = 0
        for i in range(len(counter) - 1, -1, -1):
            cnt += counter[i]
            if cnt >= k:
                return offset + i
