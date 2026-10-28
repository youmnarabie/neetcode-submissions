from collections import deque, Counter
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = Counter(students)
        queue = deque(students)
        sammies = 0
        sandwich = sandwiches[sammies]
        while True:
            if sandwich == queue[0]:
                queue.popleft()
                sammies += 1
                counts[sandwich] -= 1 
                if counts[sandwich] == 0:
                    del counts[sandwich]
                if sammies == len(sandwiches):
                    break
                sandwich = sandwiches[sammies]
            elif len(counts.keys()) == 1:
                # only one type of student left and it isn't the same as the top sandwich
                return len(queue)
            else:
                queue.append(queue.popleft())
        if len(queue):
            return len(queue)
        return 0
