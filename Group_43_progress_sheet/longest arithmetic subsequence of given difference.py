class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        store = {}
        max_subsequence = 0
        for i in range(len(arr) - 1, -1, -1):
            nuxt = arr[i] + difference
            if nuxt in store:
                store[arr[i]] = store[nuxt] + 1
            else:
                store[arr[i]] = 1

            max_subsequence = max(max_subsequence, store[arr[i]])
        
        return max_subsequence
