# Enter your code here. Read input from STDIN. Print output to STDOUT
rep = int(input())
for _ in range(rep):
    n = int(input())
    cubes = list(map(int, input().split()))
    ans = None
    for i in range(1, n-1):
        if cubes[i] > cubes[i-1] and cubes[i] > cubes[i+1]:
            ans = "No"
            break
    
    print("Yes") if not ans else print(ans)
