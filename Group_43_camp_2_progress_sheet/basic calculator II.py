class Solution:
    def calculate(self, s: str) -> int:
        s = ''.join(s.split())
        num = ""
        i = 0
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        stack = [int(num)]

        while i < len(s):
            op = s[i]
            i += 1
            num = ""
            while i < len(s) and s[i].isdigit():
                num += s[i]
                i += 1


            # compute the operations and replace them with the result
            if op == '*':
                stack.append(stack.pop() * int(num))
            elif op == '/':
                stack.append(int(stack.pop() / int(num)))
            elif op == '-':
                stack.append(-int(num))
            else:
                stack.append(int(num))
        
        return sum(stack)
