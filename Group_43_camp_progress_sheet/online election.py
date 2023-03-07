class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.lead = []
        votes = defaultdict(int)
        curr_max_vote = 0
        curr_lead = -1
        for person in persons:
            votes[person] += 1
            if votes[person] >= curr_max_vote:
                curr_max_vote = votes[person]
                curr_lead = person
            
            self.lead.append(curr_lead)

    def q(self, t: int) -> int:
        left, right = -1, len(self.times)
        while left + 1 < right:
            mid = left + (right-left) // 2
            if self.times[mid] <= t:
                left = mid
            else:
                right = mid
        
        return self.lead[left]


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)
