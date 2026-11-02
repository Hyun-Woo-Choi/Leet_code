from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:

        graph = defaultdict(list)
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course)
            in_degree[course] += 1

        
        queue = deque([i for i in range(numCourses) if in_degree[i] == 0])
        studied_count = 0

        while queue:
            curr = queue.popleft()
            studied_count += 1

            for next_course in graph[curr]:
                in_degree[next_course] -= 1
                
                if in_degree[next_course] == 0:
                    queue.append(next_course)
            
        return studied_count == numCourses