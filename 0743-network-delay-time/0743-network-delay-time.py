import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)

        for u, v, w in times:
            graph[u].append((v, w))

        dist = {}

        pq = [(0, k)] # weight, start
        heapify(pq)

        while pq:
            time, node = heapq.heappop(pq)
            
            if node in dist:
                continue
            dist[node] = time

            for neighbor, weight in graph[node]:
                if neighbor not in dist:
                    heapq.heappush(pq, (time + weight, neighbor))
            
            if len(dist) == n:
                return(max(dist.values()))
        return -1


        # pq = [(0, k)]



        # graph = defaultdict(list)

        # for u, v, w in times:
        #     graph[u].append((v, w))
        
        # pq = [(0, k)]

        # dist = {}

        # while pq:
        #     time, node = heapq.heappop(pq)

        #     if node in dist:
        #         continue
        #     dist[node] = time

        #     for neighbor, weight in graph[node]:
        #         if neighbor not in dist:
        #             heapq.heappush(pq, (time + weight, neighbor))
            
        #     if len(dist) == n:
        #         return max(dist.values())
        #     return -1
            