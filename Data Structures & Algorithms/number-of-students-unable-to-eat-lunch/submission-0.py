class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts = {0: students.count(0), 1: students.count(1)}
        print(counts)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            counts[sandwich] -= 1
        return counts[0] + counts[1]








        
