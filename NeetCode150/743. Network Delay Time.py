class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_mat = [[[float('inf'), i] for i in range(n+1)] for _ in range(n+1)]
        for time in times:
            a, b, dist = time
            adj_mat[a][b] = [dist, b]
        
        visited = set()
        hq = [[0, k]]
        
        while len(visited) < n:
#             print(visited)
            distance, current = heapq.heappop(hq)
#             print(current, distance)
            if current in visited:
                continue
            elif distance == float('inf'):
                return -1
            visited.add(current)
            for nei_distance, neighbor in adj_mat[current]:
                heapq.heappush(hq, [distance+nei_distance, neighbor])
#         print(visited)
        return distance if len(visited) == n else -1
