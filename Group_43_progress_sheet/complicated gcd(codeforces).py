intInput = lambda : int(input())
tupInput = lambda : map(int, input().strip().split())
listInput = lambda : list(map(int, input().strip().split()))
strInput = lambda : list(input().strip())

def run():
    a, b = tupInput()
    if abs(a - b) > 0:
        print(1)
    else:
        print(a)
    
    
rep = 1
for _ in range(rep):
    run()
