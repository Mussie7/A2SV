def compare(a1, a2, k):
    p1 = p2 = 0
    while p1 < len(a1) and p2 < len(a2):
        if players[a1[p1]] - players[a2[p2]] > k:
            p2 += 1
        elif players[a2[p2]] - players[a1[p1]] > k:
            p1 += 1
        else:
            break
    
    winners = []
    while p1 < len(a1) and p2 < len(a2):
        if players[a1[p1]] < players[a2[p2]]:
            winners.append(a1[p1])
            p1 += 1
        else:
            winners.append(a2[p2])
            p2 += 1
    
    winners.extend(a1[p1:])
    winners.extend(a2[p2:])
    return winners

def run(n, k, arr):
    if len(arr) == 1:
        return arr
    
    return compare(run(n//2, k, arr[:n//2]), run(n//2, k, arr[n//2:]), k)

n, k = map(int, input().split())
n = 2 ** n
players = list(map(int, input().split()))
indexArray = [i for i in range(n)]
ans = run(n, k, indexArray)
ans.sort()
print(*[index+1 for index in ans])
