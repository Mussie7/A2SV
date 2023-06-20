import collections

def parallelCourses(n, prerequisites):
    # Write your code here.
    graph = collections.defaultdict(list)
    in_degree = collections.defaultdict(int)
    for pre, course in prerequisites:
        graph[pre].append(course)
        in_degree[course] += 1

    que = collections.deque()
    course_count = 0
    for course in range(1, n+1):
        if in_degree[course] == 0:
            que.append(course)
            course_count += 1

    semester_count = 0
    while que:
        semester_count += 1
        for _ in range(len(que)):
            pre = que.popleft()
            for course in graph[pre]:
                in_degree[course] -= 1

                if in_degree[course] == 0:
                    que.append(course)
                    course_count += 1
        
    
    if course_count == n:
        return semester_count
    return -1
