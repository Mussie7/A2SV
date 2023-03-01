class Solution:
    def decoder(self, stack, rep, s, i):
        if i >= len(s):
            return

        num = ''
        while i < len(s) and s[i].isdigit():
            num += s[i]
            i += 1
        
        if num:
            rep.append(int(num))
            self.decoder(stack, rep, s, i)
            return
        
        if s[i] == '[':
            stack.append('')
        elif s[i] == ']':
            result = stack.pop() * rep.pop()
            stack[-1] += result
        else:
            stack[-1] += s[i]

        self.decoder(stack, rep, s, i+1)

    def decodeString(self, s: str) -> str:
        str_stack = ['']
        self.decoder(str_stack, [], s, 0)
        return str_stack[0]
