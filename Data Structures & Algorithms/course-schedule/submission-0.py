from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adjacency list and in_degree with plain loops
        adjacency_list = {}
        in_degree = {}
        for i in range(numCourses):
            adjacency_list[i] = []
            in_degree[i] = 0

        for course, pre in prerequisites:
            adjacency_list[pre].append(course)
            in_degree[course] += 1

        # build the starting queue with plain loops
        q = deque()
        for c in range(numCourses):
            if in_degree[c] == 0:
                q.append(c)

        processed = 0
        while q:
            c = q.popleft()
            processed += 1
            for dependent in adjacency_list[c]:
                in_degree[dependent] -= 1
                if in_degree[dependent] == 0:
                    q.append(dependent)

        return processed == numCourses