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

    
from collections import Counter


# same thing
# def cheap_destruct(n, c, orbits):
#     cost = 0
#     value = Counter(orbits).most_common()
    
#     for i in range(len(value)):
#         if value[i][1] == 1:
#             cost += len(value) - i
#             return cost
        
#         cost += min(value[i][1], c)
    
#     return cost

# rep = int(input())
# for _ in range(rep):
#     n, c = tuple(map(int, input().split()))
#     orbits = input().split()
#     print(cheap_destruct(n, c, orbits))
