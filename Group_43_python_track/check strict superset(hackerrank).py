# Enter your code here. Read input from STDIN. Print output to STDOUT
def super_set_checker():
    setA = set(input().split())
    set_list = []
    n = int(input())
    for _ in range(n):
        set_list.append(set(input().split()))

    for sets in set_list:
        if len(sets) >= len(setA):
            return False
        elif setA.intersection(sets) != sets:
            return False
    return True

print(super_set_checker())
