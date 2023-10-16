from math import sqrt

class Solution:
    def find_r2_dist(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        num_points = len(points)
        dist_matrix = [[0]*num_points for _ in range(num_points)]
        for i, point1 in enumerate(points):
            for j, point2 in enumerate(points):
                if i == j:
                    dist_matrix[i][j] = (float('inf'), i)
                    continue
                dist_matrix[i][j] = (self.find_r2_dist(point1, point2), j)
                dist_matrix[j][i] = (self.find_r2_dist(point1, point2), i)
        
        
        
        res = 0
        visit = set()
        min_heap = [(0, 0)]
        while (len(visit) < num_points):
            cost, current = heapq.heappop(min_heap)
            if current in visit:
                continue
            visit.add(current)
            res += cost
            for neighbor in range(num_points):
                if neighbor in visit:
                    continue
                heapq.heappush(min_heap, (dist_matrix[current][neighbor]))

        return res
