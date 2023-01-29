n = int(input())
cards = list(map(int, input().strip().split()))

left, right = 0, n-1
henok = wube = 0

for i in range(n):
    if i % 2:
        if cards[left] > cards[right]:
            henok += cards[left]
            left += 1
        else:
            henok += cards[right]
            right -= 1
    else:
        if cards[left] > cards[right]:
            wube += cards[left]
            left += 1
        else:
            wube += cards[right]
            right -= 1

print(wube, henok)
