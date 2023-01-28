# using bubble sort to find and put the small one at the end and then concatenating
# O(n^2) time and O(1) space
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        for i in range(len(nums)):
            nums[i] = str(nums[i])
        
        for i in range(len(nums)):
            for j in range(len(nums)-i-1):
                if nums[j] + nums[j+1] < nums[j+1] + nums[j]:
                    nums[j], nums[j+1] = nums[j+1], nums[j]
        
        return str(int(''.join(nums)))


# changing the class to change the comparator when the sort function is called
# O(nlogn) time and O(1) space
class String(str):
    def __lt__(self, other):
        return self + other > other + self

class Solution:
    def largestNumber(self, nums: [int]) -> str:
        for i in range(len(nums)):
            nums[i] = String(str(nums[i]))
        
        nums.sort()
        
        return str(int("".join(nums)))  
