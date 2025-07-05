class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals by start time
        intervals.sort(key=lambda x: x[0])
        
        # Step 2: Create output list and put first interval
        output = [intervals[0]]
        
        # Step 3: Check each interval
        for start, end in intervals[1:]:
            last_end = output[-1][1]
            
            if start <= last_end:
                # Overlapping → merge
                output[-1][1] = max(last_end, end)
            else:
                # No overlap → add to output
                output.append([start, end])
        
        return output


#Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
#Output: [[1,6],[8,10],[15,18]]
