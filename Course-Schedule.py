class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        if len ( prerequisites ) == 0 : return True
        checklist = [0] * numCourses
        
        for a, b in prerequisites :
            key = b
            flag = False
            for c, d in prerequisites :
                if prerequisites [ c-1 ] [ 0 ] == key :
                    key = d
                    flag = True
            if flag == False : 
                checklist [ b ] = 1
                checklist [ a ] = 1
            
        if checklist == [1] * numCourses : return True
        return False
