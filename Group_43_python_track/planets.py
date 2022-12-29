from collections import Counter

def cheap_destruct(n, c, orbits):
    cost = 0
    orbit_counter = Counter(orbits)
    
    for value in orbit_counter.values():
        cost += min(value, c)
    
    return cost

rep = int(input())
for _ in range(rep):
    n, c = tuple(map(int, input().split()))
    orbits = input().split()
    print(cheap_destruct(n, c, orbits))
