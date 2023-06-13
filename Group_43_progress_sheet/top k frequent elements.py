class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # first implement quicksort
        # we are using the last element as the pivot for this current quicksort implementation
        def quicksort(left, right):
            if left + 1 >= right:
                return
            
            pivot = nums[right - 1]
            swapper = left - 1
            # what the next code block does is - make sure that the elements after the swapper index have more frequency than the element at the pivot
            for i in range(left, right):
                if counter[nums[i]] <= counter[pivot]:
                    nums[swapper + 1], nums[i] = nums[i], nums[swapper + 1]
                    swapper += 1
            
            # if the current index of the pivot(swapper) is greater than n - k, i.e. the pivot element belongs in the group of k most frequent elements, sort the left half
            if swapper < n - k:
                quicksort(swapper + 1, right)
            # if the current index of the pivot(swapper) is less than n - k, i.e. the most frequent elements reside to the right, sort the right
            elif swapper > n - k:
                quicksort(left, swapper)
            
            # if we found the kth most frequent element stop sorting
            return
        

        counter = Counter(nums)
        # we will be sorting the unique elements of nums in the increasing order of their frequency
        nums = list(counter.keys())
        n = len(nums)
        quicksort(0, n)
        return nums[-k:]
