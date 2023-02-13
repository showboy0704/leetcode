class Solution:
    def shortestPathLength(self, graph: list[list[int]]) -> int:
        queue =[]
        n = len(graph)
        visited = set()
        for node in range(n):
            visited_states = 1 << node
            queue.append((node,visited_states))
            visited.add((node,visited_states))
        
        step = 0
        complete_state = (1 << n) - 1
        while queue:
            for _ in range(len(queue)):
                cur,seen_states = queue[0]
                queue=queue[1:]
                if seen_states == complete_state:
                    return step
                
                for nxt in graph[cur]:
                    new_states = seen_states | (1 << nxt)
                    if (nxt,new_states) not in visited:
                        visited.add((nxt,new_states))
                        queue.append((nxt,new_states))
            step +=1

if __name__ == '__main__':
    graph = [[1, 2, 3], [0], [0], [0]]
    print(f"{graph }")
    print('----------Answer Below----------')
    print(Solution().shortestPathLength(graph))
