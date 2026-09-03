
from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjacency_list = {}
        in_degree = {}
        for i in range(numCourses):
            adjacency_list[i]=[]
            in_degree[i]=0

        for course, pre in prerequisites:
            adjacency_list[pre].append(course)
            in_degree[course] +=1

        q= deque()
        for course in in_degree:
            if in_degree[course]==0:
                q.append(course)
        processed = 0
        while q:
            c = q.popleft()
            processed+=1
            for pre in adjacency_list[c]:
                in_degree[pre] -=1
                if in_degree[pre]==0:
                    q.append(pre)
                

        return processed == numCourses