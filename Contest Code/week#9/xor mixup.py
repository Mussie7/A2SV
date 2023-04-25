intInput = lambda : int(input())
tupInput = lambda : map(int, input().strip().split())
listInput = lambda : list(map(int, input().strip().split()))
strInput = lambda : list(input().strip())


def run():
    n = intInput()
    arr = listInput()
    print(arr[0])


rep = intInput()
for _ in range(rep):
    run()
