def legit_transformation(n: int, arr: list[str], st: list[str]) -> bool:
    transformation_dict = {}
    for i in range(n):
        if arr[i] not in transformation_dict:
            transformation_dict[arr[i]] = st[i]
        else:
            if transformation_dict[arr[i]] != st[i]:
                return False
            
    return True

rep = int(input())
for _ in range(rep):
    n = int(input())
    arr = input().split()
    st = input()
    print('YES') if legit_transformation(n, arr, st) else print('NO')
