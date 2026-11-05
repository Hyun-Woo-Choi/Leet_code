class Solution:
    def maxProbability(self, n: int, edges: list[list[int]], succProb: list[float], start_node: int, end_node: int) -> float:
        graph = defaultdict(list)

        for i in range(len(edges)):
            u, v = edges[i]
            p = succProb[i]
            graph[u].append((v, p))
            graph[v].append((u, p))
        
        max_prob = [0.0] * n
        max_prob[start_node] = 1.0

        pq = [(-1.0, start_node)]

        while pq:
            neg_p, cur_node = heapq.heappop(pq)
            cur_p = -neg_p

            if cur_node == end_node:
                return cur_p
            
            if cur_p < max_prob[cur_node]:
                continue
            
            for next_node, edge_prob in graph[cur_node]:
                next_p = cur_p * edge_prob

                if next_p > max_prob[next_node]:
                    max_prob[next_node] = next_p
                    heapq.heappush(pq, (-next_p, next_node))
        
        return 0.0
            
