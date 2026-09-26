import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # do a max heap solution

        heap = [-s for s in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = -heapq.heappop(heap)
            y = -heapq.heappop(heap)

            if x != y:
                y -= x
                heapq.heappush(heap, y)

        if len(heap) > 0:
            return -heap[0]
        else:
            return 0
        