class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        # the trick, I belive, is holding a buffer to calculate the distance. Like [0, -1] at the beginning helps you calculate the distance starting from the beginning. Now you don't have to worry about removing the actual element from the que when a smaller element comes along.
        que = collections.deque([[0,-1]])
        preSum = 0
        minLen = inf
        for index, num in enumerate(nums):
            # calculate the presum on a variable
            preSum += num
            # if found a valid subarray calculate the distance and move on to the next one
            while que and preSum - que[0][0] >= k:
                minLen = min(minLen, index - que.popleft()[1])
            
            # if the new prefix sum is smaller than the previous, remove the previous prefix sum
            while que and preSum < que[-1][0]:
                que.pop()
            
            # append the new prefix sum with it's index on the queue
            que.append([preSum, index])
        
        # don't forget to check if you didn't find any valid subarrays
        return minLen if minLen != inf else -1
