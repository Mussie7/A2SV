def run():
    def divConq(p):
        nonlocal swaps
        
        n = len(p)
        if n == 1:
            return p
        
        left = divConq(p[:n//2])
        right = divConq(p[n//2:])
        
        if not left or not right:
            return
        
        if left[-1] + 1 == right[0]:
            return left + right
        elif right[-1] + 1 == left[0]:
            swaps += 1
            return right + left
        
        return
        
    m = int(input().strip())
    perm = list(map(int, input().strip().split()))
    
    swaps = 0
    if not divConq(perm):
        print(-1)
    else:
        print(swaps)
    
rep = int(input().strip())
for _ in range(rep):
    run()
