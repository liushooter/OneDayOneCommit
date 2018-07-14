'''

            +-----+         +------+
   +--------+  B  +---------+  D   +---------+
   |        +-+---+        X+--+---+         |
   |          |          XX    |             |
+--+--+       |         XX     |           +-+--+
|  A  |       |        XX      |           | F  |
+--+--+       |      XX        |           +----+
   |          |   XXX          |
   |       +--+XXX          +--+-+
   +-------+ C  +-----------+ E  |
           +----+           +----+

'''

graph = {
    "A" : ["B", "C"],
    "B" : ["A", "C", "D"],
    "C" : ["A", "B", "D", "E"],
    "D":  ["B", "C", "E", "F"],
    "E" : ["C", "D"],
    "F" : ["D"],
 }


def BFS(graps, s):
    stack = []
    stack.append(s)
    seen = set()
    seen.add(s)
    parent = {s : None}

    while (len(stack) >0):
        vertex = stack.pop()
        nodes = graph[vertex]

        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)
                parent[w] = vertex

        print(vertex)
    return parent

# BFS(graph, "A")
parent = BFS(graph, "E")
print("-"*20)

for key in parent:
    print(key, parent[key])

v= "B"

while v != None:
    print(v)
    v= parent[v]