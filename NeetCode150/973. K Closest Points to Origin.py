class coords:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __get_magnitude(self, x, y):
        return math.sqrt((x**2 + y**2))
    
    def __eq__(self, other):
        return self.__get_magnitude(self.x, self.y) == self.__get_magnitude(other.x, other.y)
    def __lt__(self, other):
        return self.__get_magnitude(self.x, self.y) < self.__get_magnitude(other.x, other.y)
    def __gt__(self, other):
        return self.__get_magnitude(self.x, self.y) > self.__get_magnitude(other.x, other.y)
    def __le__(self, other):
        return self.__get_magnitude(self.x, self.y) <= self.__get_magnitude(other.x, other.y)
    def __ge__(self, other):
        return self.__get_magnitude(self.x, self.y) >= self.__get_magnitude(other.x, other.y)
    
    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [coords(*point) for point in points]
        heapq.heapify(heap)
        ans = []
        for i in range(k):
            point = heapq.heappop(heap)
            ans.append([point.x, point.y])
        
        return ans
