class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        answer =[]
        if not intervals:
            return False

        intervals.sort(key= lambda x:x[0])
        
        temp_start, temp_finish = intervals[0]

        for interval in intervals[1:]:
            s_int, f_int = interval[0], interval[1]
            if s_int <= temp_finish:
                temp_finish = max(temp_finish, f_int)
            else:
                answer.append([temp_start, temp_finish])
                temp_start, temp_finish = s_int, f_int
        
        answer.append([temp_start, temp_finish])
        return answer
