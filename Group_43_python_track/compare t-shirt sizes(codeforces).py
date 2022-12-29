def compare_size(t1, t2):
    if t1[-1] == 'S':
        if t2[-1] != 'S' or len(t1) > len(t2):
            return '<'
        elif len(t1) < len(t2):
            return '>'
        else:
            return '='
    elif t1[-1] == 'L':
        if t2[-1] != 'L' or len(t1) > len(t2):
            return '>'
        elif len(t1) < len(t2):
            return '<'
        else:
            return '='
    elif t2[-1] == 'S':
        return '>'
    elif t2[-1] == 'L':
        return '<'
    else:
        return '='



rep = int(input())
for _ in range(rep):
    t_shirts = input().split()
    print(compare_size(t_shirts[0], t_shirts[1]))
