from collections import deque

class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # initiate and set array to count students' preference
        cnt = [0, 0]
        for type in students:
            cnt[type] += 1
        
        # use queue for better pop opertaion
        sand = deque(sandwiches)
        stud = deque(students)
        
        while len(stud) and len(sand):
            # case current student prefers current sandwich
            if stud[0] == sand[0]:
                type = sand.popleft()
                cnt[type] -= 1
                stud.popleft()
            else:
                # case nobody prefers current sandwich
                if cnt[sand[0]] == 0:
                    break
                    
                # send the student back to the queue
                s = stud.popleft()
                stud.append(s)
        
        return len(stud)
        