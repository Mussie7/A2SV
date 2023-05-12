class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        n, m = len(nums1), len(nums2)
        heap = [[nums1[0] + nums2[0], [0, 0]]]
        pairs = []
        while heap and len(pairs) < k:
            _, (i, j) = heapq.heappop(heap)
            pairs.append([nums1[i], nums2[j]])

            if j < m - 1:
                heapq.heappush(heap, [nums1[i] + nums2[j + 1], [i, j + 1]])
            
            # did this using a visited set first
            # besides the first second array element the other elements will get the chance with the elements of the first array from the above if condition
            if j == 0 and i < n - 1:
                heapq.heappush(heap, [nums1[i + 1] + nums2[j], [i + 1, j]])
        
        return pairs
