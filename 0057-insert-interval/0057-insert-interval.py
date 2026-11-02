class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        left, right = [], []
        ns, ne = newInterval

        for interval in intervals:
            if interval[1] < ns:
                # newInterval보다 완전히 왼쪽
                left.append(interval)
            elif interval[0] > ne:
                # newInterval보다 완전히 오른쪽
                right.append(interval)
            else:
                # 겹치는 구간 -> newInterval 범위를 계속 확장
                ns = min(ns, interval[0])
                ne = max(ne, interval[1])

        return left + [[ns, ne]] + right