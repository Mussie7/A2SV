class Solution:
    def countHomogenous(self, s: str) -> int:
        homogenous_count = 0
        index = 0
        while index < len(s):
            curr_char = s[index]
            index += 1
            curr_char_count = 1
            while index < len(s) and s[index] == curr_char:
                index += 1
                curr_char_count += 1
            
            homogenous_count += (curr_char_count * (curr_char_count + 1)) // 2
        
        return homogenous_count % (10 ** 9 + 7)