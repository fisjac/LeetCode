from collections import deque, defaultdict
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:

        def buildGraph(n, edges): # build red and blue adjacency lists
            graph = defaultdict(list)
            for i in range(n): graph[i] = []
            for edge in edges: graph[edge[0]].append(edge[1])
            return graph

        edges = {
            'red': buildGraph(n, redEdges),
            'blue': buildGraph(n, blueEdges)
            }
        queue = deque()
        queue.append((0,'blue',0))
        queue.append((0,'red',0))
        results = [-1 for _ in range(n)]
        visited = set()

        while len(queue) > 0 and min(results) < 0:
            (currNode, color, distance) = queue.popleft()
            # print(currNode, color)
            new_color ='blue' if color=='red' else 'red'
            visited.add((currNode,color))
            next_edges = edges[color][currNode]
            if results[currNode] == -1: results[currNode] = distance
            for edge in next_edges:
                # print('new edge', edge, new_color)
                if (edge, new_color) not in visited:
                    # print('adding')
                    queue.append((edge, new_color, distance + 1))
        # while queue has length and target <= n
            # if currNode == target results[target] == length and increment target + 1
            # popleft from queue read edges from corresponding adjacency list
            # if edge node not in visited add add node to queue
        return results
