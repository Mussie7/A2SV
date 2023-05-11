#User function Template for python3
import collections

class Solution:
    def findOrder(self,alien_dict, n, k):
        graph = collections.defaultdict(list)
        start = {}
        que = set()
        for word in alien_dict:
            for char in word:
                start[char] = 0
                que.add(char)
                
        for i in range(n-1):
            word, nuxt = alien_dict[i], alien_dict[i+1]
            index = 0
            while index < len(word) and word[index] == nuxt[index]:
                index += 1
            
            if index < len(word):
                graph[word[index]].append(nuxt[index])
                start[nuxt[index]] += 1
                que.discard(nuxt[index])
        
        que = collections.deque(que)
        alphabet = ''
        while que:
            char = que.popleft()
            alphabet += char
            for child in graph[char]:
                start[child] -= 1
                if start[child] == 0:
                    que.append(child)

        return (alphabet)
