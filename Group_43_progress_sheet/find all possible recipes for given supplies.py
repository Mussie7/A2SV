#Topological sort using bfs
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(set)
        ing_count = Counter()
        for i, ingredient in enumerate(ingredients):
            for ing in ingredient:
                graph[ing].add(recipes[i])
        
            ing_count[recipes[i]] = len(ingredients[i])
        
        que = deque(supplies)
        cooked = []
        while que:
            done = que.popleft()
            for dependent in graph[done]:
                ing_count[dependent] -= 1

                if ing_count[dependent] == 0:
                    cooked.append(dependent)
                    que.append(dependent)
        
        return cooked

    
# Topological sort using dfs
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        def dfs(food):
            recipe_map[food][1] = 1
            for gredient in ingredients[recipe_map[food][0]]:
                if gredient in supplies or gredient in cooked:
                    continue
                elif gredient not in recipe_map or ((recipe_map[gredient][1] == 1 or not dfs(gredient))):
                    return False
            
            cooked.add(food)
            return True

        supplies = set(supplies)
        recipe_map = {recipe: [index, 0] for index, recipe in enumerate(recipes)}
        cooked = set()

        for recipe in recipes:
            if recipe_map[recipe][1] == 0:
                dfs(recipe)
        
        return cooked
