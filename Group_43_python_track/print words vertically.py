class Solution:
    def printVertically(self, s: str) -> List[str]:
        s_list = s.split()
        # finding the length of the longest word in the string array
        limit_len = len(max(s_list, key=len))
        
        for i in range(len(s_list)):
            # filling the shorter words with space until they have the same length as the longest word
            s_list[i] += ' ' * (limit_len - len(s_list[i]))

        output = []
        for column in zip(*s_list):
            # removing any trailing spaces
            output.append("".join(column).rstrip())
        
        return output
