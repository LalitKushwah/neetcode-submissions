class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = None

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        counts =  Counter(students)
        print(counts)
        for sandwich in sandwiches:
            if counts[sandwich] == 0:
                break
            counts[sandwich] -= 1
            print(counts)
        print(counts)
        return counts[0] + counts[1]








        
