import heapq
class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[0])

        rooms = [intervals[0][1]]
        heapq.heapify(rooms)

        for start, end in intervals[1:]:

            if rooms[0] <= start:
                heapq.heappop(rooms)
            
            heapq.heappush(rooms, end)
        
        return len(rooms)