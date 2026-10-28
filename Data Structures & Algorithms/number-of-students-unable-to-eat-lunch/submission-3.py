from collections import deque, Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        for sandwich in sandwiches:
            if counts[sandwich] > 0:
                counts[sandwich] -= 1 
            elif sandwich == 0:
                return counts[1]
            else:
                return counts[0]
        return 0 
