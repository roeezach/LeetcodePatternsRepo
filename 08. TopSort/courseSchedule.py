# Topological Sort Template
# Problem: Course Schedule

from collections import defaultdict, deque
from typing import List
    # the main thing to note here is a detection of a cycle, which is represent by a course prequisite.
def can_finish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    prerequisites_dict = { i : [] for i in range(numCourses)}
    for course,pre_course in prerequisites:
        prerequisites_dict[course].append(pre_course)
    visited = set()
    
    def dfs(course):
        if course in visited:
            return False
        if prerequisites_dict[course] == []:
            return True
        visited.add(course)
        for pre_course in prerequisites_dict[course]:
            if not dfs(pre_course) : 
                return False
        visited.remove(course)
        prerequisites_dict[course] = []
        return True

    # in case the graph is not connected 
    for course in range(numCourses):
        if not dfs(course) : return False
    return True 
# Unit tests

output = can_finish(2, [[1, 0]])
print("Actual Output:", output)
assert output == True

assert can_finish(2, [[1, 0], [0, 1]]) == False
