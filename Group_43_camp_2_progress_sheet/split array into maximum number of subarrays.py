class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        min_score = nums[0]
        for num in nums:
            min_score &= num

        # The minimum number we can get by 'AND'ing a list of numbers is the minimum number in the array or less
        # Therefore we can't break up an array and get a subarray that can give us a lesser value after 'AND'ing its elements than we would get by 'AND'ing the elements of the original array
        if min_score > 0:
            return 1

        # If the value we get by 'AND'ing the elements of the array is zero find out how many subarrays can yield a value of zero when its elements are 'AND'ed
        subarray_count = 0
        # bit representation of this number is interesting. not really
        curr_score = 1048575
        for num in nums:
            curr_score &= num
            if curr_score == 0:
                subarray_count += 1
                curr_score = 1048575
        
        return subarray_count
