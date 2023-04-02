class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        subarray_count = 0
        for i in range(len(nums)):
            if nums[i] % k:
                continue
            
            cur_gcd = nums[i]
            for j in range(i, len(nums)):
                if nums[j] % k:
                    break
                cur_gcd = gcd(max(cur_gcd, nums[j]), min(cur_gcd, nums[j]))

                if cur_gcd == k:
                    subarray_count += 1
        
        return subarray_count
