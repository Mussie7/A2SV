# O(nlog(k)) time and O(n) space complexities
# created a new class that computes less than as greater than
class String:
	def __init__(self, st):
		self.st = st
		
	def __lt__(self, other):
		return self.st > other.st

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        word_map = Counter(words)
        for word in word_map:
            # when k elements are added, add the new word and remove the smallest until then add all the words
            if len(heap) == k:
                heapq.heappushpop(heap, (word_map[word], String(word)))
            else:
                heapq.heappush(heap, (word_map[word], String(word)))
        
        # since the heap is a min-heap I have to reverse the order
        return reversed([heapq.heappop(heap)[1].st for _ in range(k)])



# cleaner implementation with o(nlog(n)) time and O(n) space
# this time you don't need to create a new class, that computes less than as greater than, because if the frequency is the same the smallest word will be on top. Why? because it is a min-heap.
# you also don't need to reverse the output at the end
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        heap = []
        word_map = Counter(words)
        for word in word_map:
            heapq.heappush(heap, (-word_map[word], word))
        
        return [heapq.heappop(heap)[1] for _ in range(k)]
