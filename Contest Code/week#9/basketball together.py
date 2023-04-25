def run():
    n, d = map(int, input().split())
    arr = list(map(int, input().split()))
    arr.sort()

    right = n - 1
    teams = players = 0
    while players <= n:
        players += (d // arr[right]) + 1
        if players <= n:
            teams += 1
        
        right -= 1
        
    
    print(teams)
    



run()
