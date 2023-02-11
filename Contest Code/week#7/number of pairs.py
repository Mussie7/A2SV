b = int(input())
boys = list(map(int, input().split()))
g = int(input())
girls = list(map(int, input().split()))

boys.sort()
girls.sort()

pointer1 = pointer2 = 0
pairs = 0

while pointer1 < b and pointer2 < g:
    if boys[pointer1] - girls[pointer2] < -1:
        pointer1 += 1
    elif boys[pointer1] - girls[pointer2] > 1:
        pointer2 += 1
    else:
        pairs += 1
        pointer1 += 1
        pointer2 += 1

print(pairs)
