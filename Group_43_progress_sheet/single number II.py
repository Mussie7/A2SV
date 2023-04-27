class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        pos_bit_counter = Counter()
        neg_bit_counter = Counter()
        for num in nums:
            if num < 0:
                curr_counter = neg_bit_counter
            else:
                curr_counter = pos_bit_counter
            
            num = abs(num)
            count = 0
            while 1 << count <= num:
                if 1 << count & num:
                    curr_counter[count] += 1
                count += 1
        
        target = 0
        for bit in pos_bit_counter:
            if pos_bit_counter[bit] % 3:
                target ^= (1 << bit)

        if not target:
            for bit in neg_bit_counter:
                if neg_bit_counter[bit] % 3:
                    target ^= (1 << bit)
            
            return -target
        return target
