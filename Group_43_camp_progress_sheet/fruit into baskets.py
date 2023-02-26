class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        left = 0
        maxFruits = 0
        basket = {}

        for right in range(len(fruits)):
            basket[fruits[right]] = right
            if len(basket) > 2:
                for fruit in basket:
                    if fruit != fruits[right-1] and fruit != fruits[right]:
                        left = basket[fruit] + 1
                        del basket[fruit]
                        break
            
            maxFruits = max(right-left+1, maxFruits)

        return maxFruits
