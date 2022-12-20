# Enter your code here. Read input from STDIN. Print output to STDOUT
n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
setA = set(map(int, input().split()))
setB = set(map(int, input().split()))

happiness = 0
for i in range(n):
    if arr[i] in setA:
        happiness += 1
    if arr[i] in setB:
        happiness -= 1

print(happiness)
