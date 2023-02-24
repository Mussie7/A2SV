class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        minStack = []
        counter = Counter(s)
        seen = set()

        for char in s:
            if char in seen:
                counter[char] -= 1
                continue

            while minStack and char < minStack[-1] and counter[minStack[-1]] > 1:
                cur = minStack.pop()
                seen.remove(cur)
                counter[cur] -= 1
            
            minStack.append(char)
            seen.add(char)
        
        return ''.join(minStack)
