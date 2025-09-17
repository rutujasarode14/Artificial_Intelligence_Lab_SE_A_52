import heapq

class Node:
    def __init__(self, name, parent=None, g=0, h=0):
        self.name = name
        self.parent = parent
        self.g = g  
        self.h = h  
        self.f = g + h 

    def __lt__(self, other):  
        return self.f < other.f

def astar_search(graph, heuristics, start, goal):
    open_list = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristics[start])
    heapq.heappush(open_list, start_node)

    while open_list:
        current = heapq.heappop(open_list)

        if current.name == goal:
            path = []
            total_cost = current.g
            while current:
                path.append(current.name)
                current = current.parent
            return path[::-1], total_cost  

        closed_set.add(current.name)

        for neighbor, cost in graph[current.name].items():
            if neighbor in closed_set:
                continue

            g = current.g + cost
            h = heuristics[neighbor]
            neighbor_node = Node(neighbor, current, g, h)

            
            if any(open_node.name == neighbor and open_node.f <= neighbor_node.f for open_node in open_list):
                continue

            heapq.heappush(open_list, neighbor_node)

    return None, float('inf')


graph = {
          'S': {'A': 1, 'B': 4},
          'A': {'B': 2, 'C': 5, 'D': 12},
          'B': {'C': 2},
          'C': {'D': 3, 'G': 7},
          'D': {'G': 2},
          'G': {}
}


heuristics = {
   
     
         'S': 7, 'A': 6, 'B': 4,
         'C': 2, 'D': 1, 'G': 0
     
}


start, goal = 'A', 'G'
path, total_cost = astar_search(graph, heuristics, start, goal)
print(f"Shortest path from {start} to {goal}: {path}")
print(f"Total cost: {total_cost}")

