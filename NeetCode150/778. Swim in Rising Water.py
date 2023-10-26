class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        grid_size = len(grid)
        min_times = [[float('inf') for _ in range(grid_size)] for _ in range(grid_size)]
        min_heap = [[grid[0][0], 0, 0]]
        visited = set()
        while len(visited) < grid_size*grid_size:
            current_time, current_y, current_x = heapq.heappop(min_heap)
            if (current_y, current_x) in visited:
                continue
            min_times[current_y][current_x] = min(current_time, min_times[current_y][current_x])
            visited.add((current_y, current_x))
            if current_x-1 > -1:
                heapq.heappush(min_heap, [max(current_time, grid[current_y][current_x-1]), current_y, current_x-1])
            if current_y-1 > -1:
                heapq.heappush(min_heap, [max(current_time, grid[current_y-1][current_x]), current_y-1, current_x])
            if current_x+1 < grid_size:
                heapq.heappush(min_heap, [max(current_time, grid[current_y][current_x+1]), current_y, current_x+1])
            if current_y+1 < grid_size:
                heapq.heappush(min_heap, [max(current_time, grid[current_y+1][current_x]), current_y+1, current_x])
        return min_times[grid_size-1][grid_size-1]
