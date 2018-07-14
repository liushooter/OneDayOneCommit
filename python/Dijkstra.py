#coding: UTF-8

'''
https://www.bilibili.com/video/av25829980
Dijkstra算法是BFS的升级版。当一个图中的每条边都加上权值后，BFS就没办法求一个点到另一个点的最短路径了。
这时候，需要用到Dijkstra算法。从最基本原理上讲，把BFS改成Dijkstra算法，只需要把“队列”改成“优先队列”就可以了。
介绍BFS转Dijkstra的具体过程，包括优先队列的用法、代码实现。

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

import heapq

graph = {
    "A" : {"B":5, "C": 1},
    "B" : {"A":5, "C":2, "D":1},
    "C" : {"A":1, "B":2, "D":4, "E":8},
    "D" : {"B":1, "C":4, "E":3, "F":6},
    "E" : {"C":8, "D":3},
    "F" : {"D":6},
 }


def init_distance(graph, s):
    distance = {s:0}

    for vertex in graph:
        if vertex != s:
            distance[vertex]= float("inf") # math.inf python3.5

    return distance


def Dijkstra(graps, s):
    pqueue = []
    heapq.heappush(pqueue, (0,s))
    seen = set()
    parent = {s: None}
    distance = init_distance(graph, s)

    while (len(pqueue) >0):
        pair =  heapq.heappop(pqueue)
        dist = pair[0]
        vertex = pair[1]
        seen.add(vertex)

        nodes = graph[vertex].keys()

        for w in nodes:
            if w not in seen:
                if dist + graph[vertex][w] < distance[w]:
                    heapq.heappush(pqueue, (dist + graph[vertex][w], w))
                    parent[w]= vertex
                    distance[w] = dist +graph[vertex][w]

    return parent, distance

parent, distance = Dijkstra(graph, "A")

print(parent)
print(distance)