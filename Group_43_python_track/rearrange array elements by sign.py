class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        rearranged = [0] * len(nums)
        pos, neg = 0, 1

        for num in nums:
            if num > 0:
                rearranged[pos] = num
                pos += 2
            else:
                rearranged[neg] = num
                neg += 2
        
        return rearranged
