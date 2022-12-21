class Solution:
    def freqAlphabets(self, s: str) -> str:
        st, output, jump = list(s), [], 0
        for i in range(len(st)-1, -1, -1):
            if jump:
                jump -= 1
                continue
            
            if st[i].isnumeric():
                output.append(chr(96 + int(st[i])))
            else:
                output.append(chr(96 + int(st[i-2] + st[i-1])))
                jump = 2
        
        return "".join(output[::-1])
