def create_graph(links):
    graph = {}

    for tup in links:
        if tup[0] in graph:
            graph[tup[0]].append(tup[1]) 
        else:
            graph[tup[0]] = []
            graph[tup[0]].append(tup[1])
    
    return graph

links = [
    ('Mumbai', 'Paris'),
    ('Mumbai', 'Dubai'),
    ('Paris', 'Dubai'),
    ('Paris', 'New York'),
    ('Dubai', 'New York'),
    ('New York', 'Toronto')
]

newgraph = create_graph(links)
print(newgraph)
