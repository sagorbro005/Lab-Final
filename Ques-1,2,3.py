
inputFile = open('input1-3.txt', 'r')
f_line = list(map(int, inputFile.readline().split(' ')))
n_vertices, m_edges = f_line[0], f_line[1]
dict1 = {}
for i in range(m_edges):
    graph = inputFile.readline().strip().split('^')
    ver1, ver2 = graph
    try:
        dict1[ver1].append(ver2)
    except KeyError:
        dict1[ver1] = [ver2]
    try:
        dict1[ver2].append(ver1)
    except KeyError:
        dict1[ver2] = [ver1]
start_vertex = inputFile.readline().strip()
visited = {start_vertex: 0}
queue = [start_vertex]
while queue:
    current_vertex = queue.pop(0)
    for adjacency_vertex in dict1[current_vertex]:
        if adjacency_vertex not in visited:
            visited[adjacency_vertex] = visited[current_vertex] + 1
            queue.append(adjacency_vertex)
todays = [city for city, distance in visited.items() if distance % 2 == 0]
tomorrows = [city for city, distance in visited.items() if distance % 2 != 0]

outputFile = open('output1-3.txt', 'w')
outputFile.write("Today's delivery: " + ', '.join(todays) + "\n")
outputFile.write("Tomorrow's delivery: " + ', '.join(tomorrows) + "\n")

