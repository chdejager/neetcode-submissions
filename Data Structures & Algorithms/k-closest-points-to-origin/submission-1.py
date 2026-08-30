class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []

        for x, y in points:
            distance_squared = x**2 + y**2
            heapq.heappush(heap, (-distance_squared, [x, y]))

        while len(heap) > k:
            heapq.heappop(heap)
        
        result = []
        for item in heap:
            dist, point = item 
            result.append(point)
        return result
