class Solution:
    def distributer(self, index, k, cur_max):
        if index == len(self.cookies):
            self.unfairness = min(self.unfairness, cur_max)
            return
        
        for i in range(k):
            if self.unfairness <= cur_max:
                break

            self.distribution[i] += self.cookies[index]
            self.distributer(index + 1, k, max(self.distribution)
            self.distribution[i] -= self.cookies[index]
        
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)
        self.cookies = cookies
        self.distribution = [0] * k
        self.unfairness = sum(self.cookies)
        self.distributer(0, k, 0)

        return self.unfairness
