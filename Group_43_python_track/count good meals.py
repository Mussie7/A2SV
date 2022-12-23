class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        powers_of_2 = set()
        n = 22
        for i in range(n):
            powers_of_2.add(2**i)
        
        meals = {}
        for meal in deliciousness:
            if meal in meals:
                meals[meal] += 1
            else:
                meals[meal] = 1

        output = 0
        for meal in deliciousness:
            for power in powers_of_2:
                if power - meal in meals:
                    if meal * 2 == power:
                        output += meals[meal] - 1
                    else:
                        output += meals[power - meal]
            meals[meal] -= 1
        
        return output % (10**9 + 7)
