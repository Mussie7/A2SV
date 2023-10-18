class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        minimum, maximum = min(nums), max(nums)
        mean = minimum + math.ceil((maximum - minimum) / 2)
        minimum = min(mean, minimum + k)
        maximum = max(mean, maximum - k)
        return maximum - minimum
