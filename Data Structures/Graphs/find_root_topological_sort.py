def find_dag_root(graph):
    # Initialize the set of potential root vertices
    roots = set(graph.keys())
    
    # Remove vertices with incoming edges
    for vertex in graph:
        for neighbor in graph[vertex]:
            if neighbor in roots:
                roots.remove(neighbor)
    
    # Check if there is a single root or no root
    if len(roots) == 1:
        return roots.pop()
    else:
        return None
    
if __name__ == "__main__":
    