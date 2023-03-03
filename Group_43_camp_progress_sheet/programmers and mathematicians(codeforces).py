# math
def run():
    a, b = map(int, input().split())
    print(min(a, b, (a+b)//4))
    
    
rep = int(input())
for _ in range(rep):
    run()
    
# bs
def run():
    a, b = map(int, input().split())
    left, right = -1, (a+b) // 4 + 1
    while left + 1 < right:
        mid = left + (right-left) // 2
        if mid <= min(a, b):
            left = mid
        else:
            right = mid
    
    print(left)
    
    
rep = int(input())
for _ in range(rep):
    run()
