class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not nums2:
            return

        l = m - 1
        r = n - 1
        for i in range(m+n - 1, -1, -1):
            if r < 0:
                return
            if l < 0:
                nums1[i] = nums2[r]
                r -= 1
                continue
                
            if nums1[l] <= nums2[r]:
                nums1[i] = nums2[r]
                r -= 1
            else:
                nums1[i] = nums1[l]
                l -= 1
