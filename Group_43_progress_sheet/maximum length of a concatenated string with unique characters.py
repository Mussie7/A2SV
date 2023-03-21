class Solution:
    def duplicateCheck(self, str_arr):
        curr_str = ''.join(str_arr)
        if len(set(curr_str)) != len(curr_str):
            return 0
        else:
            return len(curr_str)

    def countValidStrings(self, index, curr, length):
        self.max_len = max(self.max_len, length)
        if index == len(self.arr):
            return
        
        curr.append(self.arr[index])
        check = self.duplicateCheck(curr)
        if check:
            self.countValidStrings(index + 1, curr, check)
        curr.pop()
        self.countValidStrings(index + 1, curr, length)
        

    def maxLength(self, arr: List[str]) -> int:
        self.arr = arr
        self.max_len = 0
        self.countValidStrings(0, [], 0)
        return self.max_len
