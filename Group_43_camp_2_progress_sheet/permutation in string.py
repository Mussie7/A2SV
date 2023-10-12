class Solution:
    # approach 1 - O(26N) = O(N) time complexity
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n, m = len(s1), len(s2)
        if n > m:
            return False

        counter1 = Counter(s1)
        left, right = 0, 0
        counter2 = Counter()
        while right < m:
            counter2[s2[right]] += 1
            if right - left + 1 > n:
                counter2[s2[left]] -= 1
                left += 1
            
            if counter1 == counter2:
                return True
            
            right += 1
        
        return False

    # approach 2 - O(N) time complexity
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        offset = ord('a')
        charArray1 = [0] * 26
        charArray2 = [0] * 26
        for i in range(len(s1)):
            char1 = s1[i]
            char2 = s2[i]
            charArray1[ord(char1) - offset] += 1
            charArray2[ord(char2) - offset] += 1
        
        count = 0
        for i in range(len(charArray1)):
            count += int(charArray1[i] == charArray2[i])
        
        if count == 26:
            return True

        for i in range(len(s1), len(s2)):
            idx = ord(s2[i]) - offset
            charArray2[idx] += 1
            if charArray2[idx] - 1 == charArray1[idx]:
                count -= 1
            elif charArray2[idx] == charArray1[idx]:
                count += 1
            
            idx = ord(s2[i - len(s1)]) - offset
            charArray2[idx] -= 1
            if charArray2[idx] + 1 == charArray1[idx]:
                count -= 1
            elif charArray2[idx] == charArray1[idx]:
                count += 1
            
            if count == 26:
                return True
        
        return False
