
def isSafe(graph,v,color,c,V):
    for i in range(V):
        if graph[v][i] and c == color[i]:
            return False    
    return True

def graphColorUtil(graph,m,color,v,V):

    if v == V:
        return True
    
    for c in range(1,m+1):
        if isSafe(graph,v,color,c,V):
            color[v] = c

            if graphColorUtil(graph,m,color,v+1,V) == True:
                return True
            

            color[v] = 0

def graphColoring(graph,m,V):
    
    color = [0 for i in range(V)]
    if graphColorUtil(graph,m,color,0,V) == False:
        print("Solution does not exist")
        return False
    
    print(color)
    return True   

graph = [[0,1,1,1],[1,0,1,0],[1,1,0,1],[1,0,1,0]]

m = 3 # no.of colors
V = 4 # no.of vertices

graphColoring(graph,m,V)