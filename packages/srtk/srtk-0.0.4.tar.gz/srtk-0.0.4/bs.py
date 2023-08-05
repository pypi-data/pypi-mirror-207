from collections import deque
from heapq import heappush, heappop

def beam_search(graph, start_node, beam_width, k_hops):
    # Initialize the beam queue with the start node
    beam_queue = [(0, [start_node])]
    
    # Initialize the results list
    results = []
    
    for _ in range(k_hops):
        # Create a new beam queue for the next iteration
        new_beam_queue = []

        while beam_queue:
            # Get the path with the highest score from the beam queue
            score, path = heappop(beam_queue)
            
            # Get the last node in the path
            current_node = path[-1]

            # Check if we have visited all neighbors
            if current_node not in graph:
                continue

            # Iterate through the neighbors of the current node
            for neighbor, weight in graph[current_node]:
                if neighbor not in path:
                    # Calculate the new path score
                    new_score = score + weight

                    # Create a new path
                    new_path = path + [neighbor]

                    # Add the new path to the new beam queue
                    heappush(new_beam_queue, (-new_score, new_path))

        # Update the beam queue with the top-k paths from the new beam queue
        beam_queue = sorted(new_beam_queue, reverse=True)[:beam_width]

    # Add the final paths to the results list
    results.extend(path for _, path in beam_queue)

    return results

# Example graph as an adjacency list
graph = {
    'A': [('B', 2), ('C', 3)],
    'B': [('D', 5), ('E', 1)],
    'C': [('D', 4), ('E', 6)],
    'D': [('F', 1)],
    'E': [('F', 2)]
}

# Test the beam search algorithm
start_node = 'A'
beam_width = 2
k_hops = 3
paths = beam_search(graph, start_node, beam_width, k_hops)
print("Paths with highest scores within {} hops:".format(k_hops))
for path in paths:
    print(" -> ".join(path))
