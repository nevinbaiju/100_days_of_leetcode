class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_stack = set()
        completed = set()
        prereq_dict = {}
        for i in range(numCourses):
            prereq_dict[i] = []
        
        for subject, prerequisite in prerequisites:
            prereq_dict[subject].append(prerequisite)
        
        def dfs(course):
            if course in in_stack:
                return False
            else:
                in_stack.add(course)
                for prerequisite in prereq_dict[course]:
                    
                    if course not in completed and not dfs(prerequisite):
                        return False
                in_stack.remove(course)
                completed.add(course)
                
                return True
            
        for course in prereq_dict.keys():
            if not dfs(course):
                return False
        
        return True
