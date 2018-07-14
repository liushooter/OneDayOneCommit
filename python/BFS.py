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

    while (len(stack) >0):
        vertex = stack.pop()
        nodes = graph[vertex]

        for w in nodes:
            if w not in seen:
                stack.append(w)
                seen.add(w)

        print(vertex)

BFS(graph, "A")
print("-"*20)
BFS(graph, "E")
