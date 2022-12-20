# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
room_no = list(map(int, input().split()))
possible_room, not_room = set(), set()
for i in range(len(room_no)):
    if room_no[i] in not_room:
        continue
    
    if room_no[i] in possible_room:
        possible_room.remove(room_no[i])
        not_room.add(room_no[i])
    else:
        possible_room.add(room_no[i])

print(possible_room.pop())
