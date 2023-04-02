intInput = lambda : int(input())
tupInput = lambda : map(int, input().strip().split())
listInput = lambda : list(map(int, input().strip().split()))
strInput = lambda : list(input().strip())

def run():
    x = intInput()
    y = 1
    while not x & y:
        y <<= 1
    
    mask = 1
    while not x ^ y:
        if not y & mask:
            y ^= mask
        mask <<= 1
    
    print(y)
    
rep = intInput()
for _ in range(rep):
    run()
