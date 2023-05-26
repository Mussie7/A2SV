class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        dec_stack = []
        found = False
        for i in range(len(arr)-1, -1, -1):
            while dec_stack and arr[i] >= dec_stack[-1][0]:
                if arr[i] > dec_stack[-1][0]:
                    found = True
                    swap = dec_stack.pop()[1]
                else:
                    dec_stack.pop()
            
            if found:
                arr[i], arr[swap] = arr[swap], arr[i]
                break
            
            dec_stack.append([arr[i], i])
        
        return arr
