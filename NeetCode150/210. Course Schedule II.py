class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        in_stack = set()
        completed = set()
        order = []
        prereq_dict = {}
        for i in range(numCourses):
            prereq_dict[i] = []
        
        for subject, prerequisite in prerequisites:
            prereq_dict[subject].append(prerequisite)
        
        def dfs(course):
            if course in in_stack:
                return False
            else:
                if course in completed:
                    return True
                else:
                    in_stack.add(course)
                    for prerequisite in prereq_dict[course]:    
                        if not dfs(prerequisite):
                            return False
                    in_stack.remove(course)
                    completed.add(course)
                    order.append(course)
                
                return True
            
        for course in prereq_dict.keys():
            if not dfs(course):
                return []
        
        return order
