class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()

        current = intervals[0]
        result = []

        for interval in intervals[1:]:
            x1, y1 = current
            x2, y2 = interval

            if y1 >= x2:
                y1 = max(y1, y2)
                current = [x1, y1]
            else:
                result.append(current)
                current = interval
            
        result.append(current)
        
        return result
