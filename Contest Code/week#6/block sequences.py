n, m = map(int, input().split())
heights = list(map(int, input().split()))
heights.sort()

remove = sum(heights) - n
found_height = 0
for i in range(n):
    if heights[i] > found_height:
        found_height += 1

print(remove - (max(heights) - found_height))
