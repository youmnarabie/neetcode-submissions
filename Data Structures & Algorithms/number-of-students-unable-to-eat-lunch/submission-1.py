from collections import deque, Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        queue = deque(students)
        sammies = deque(sandwiches)
        sandwich = sammies[0]
        while True:
            if sandwich == queue[0]:
                queue.popleft()
                sammies.popleft()
                counts[sandwich] -= 1 
                if counts[sandwich] == 0:
                    del counts[sandwich]
                if len(sammies) == 0:
                    break
                sandwich = sammies[0]
            elif len(counts.keys()) == 1 and len(sammies) > 0:
                while queue[0] == sammies[0]:
                    queue.popleft()
                    sammies.popleft()
                    counts[sandwich] -= 1 
                    if counts[sandwich] == 0:
                        del counts[sandwich]
                break
            else:
                queue.append(queue.popleft())
        if len(counts) != 0:
            return counts.most_common()[0][1]
        elif len(sammies) > 0:
            return len(sammies)
        return 0
