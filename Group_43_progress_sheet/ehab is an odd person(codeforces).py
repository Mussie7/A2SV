n = int(input())
arr = list(map(int, input().split()))

odd = even = False
for num in arr:
    odd = odd or num % 2 == 1
    even = even or num % 2 == 0
    
if odd and even:
    print(*sorted(arr))
else:
    print(*arr)
