class Solution:
    def stupify(self, large: str, small: str) -> str:
        add = "0"
        for i in range(len(large)):
            temp = str(int(large[-i-1]) * int(small))
            temp += '0' * i
            add = str(int(add) + int(temp))
        
        return add

    def multiply(self, num1: str, num2: str) -> str:
        small = min(num1, num2)
        large = max(num1, num2)
        add = "0"
        
        for i in range(len(small)):
            temp = self.stupify(large, small[-i-1])
            temp += "0" * i
            add = str(int(add) + int(temp))
        
        return add
