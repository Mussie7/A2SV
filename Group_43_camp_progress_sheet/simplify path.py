class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = ['']
        path = path.split('/')
        for pat in path:
            if pat == '' or pat == '.'or (pat == '..' and len(stack) <= 1):
                continue
            elif pat == '..':
                stack.pop()
            else:
                stack.append(pat)
        
        return '/'.join(stack) if len(stack) > 1 else '/'
