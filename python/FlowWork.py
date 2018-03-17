# https://en.wikipedia.org/wiki/Ford%E2%80%93Fulkerson_algorithm
# Ford–Fulkerson方法（Ford-Fulkerson method）或 Ford–Fulkerson算法（FFA）是一类计算网络流的最大流的贪心算法。
# 之所以称之为“方法”而不是“算法”，是因为它寻找增广路径的方式并不是完全确定的，而是有几种不同时间复杂度的实现方式[1][2]它在1956年由L.R.Ford,Jr. 及 D.R.Fulkerson[3]发表。
# “Ford–Fulkerson”这个名词通常也用于Edmonds–Karp算法，这是一个特殊的Ford–Fulkerson算法实现。

class Edge(object):
    def __init__(self, u, v, w):
        self.source = u
        self.sink = v
        self.capacity = w
    def __repr__(self):
        return "%s->%s:%s" % (self.source, self.sink, self.capacity)

class FlowNetwork(object):
    def __init__(self):
        self.adj = {}
        self.flow = {}

    def add_vertex(self, vertex):
        self.adj[vertex] = []

    def get_edges(self, v):
        return self.adj[v]

    def add_edge(self, u, v, w=0):
        if u == v:
            raise ValueError("u == v")
        edge = Edge(u,v,w)
        redge = Edge(v,u,0)
        edge.redge = redge
        redge.redge = edge
        self.adj[u].append(edge)
        self.adj[v].append(redge)
        self.flow[edge] = 0
        self.flow[redge] = 0

    def find_path(self, source, sink, path):

        if source == sink:
            return path
        for edge in self.get_edges(source):
            residual = edge.capacity - self.flow[edge]
            if residual > 0 and edge not in path:
                result = self.find_path( edge.sink, sink, path + [edge])
                if result != None:
                    return result

    def max_flow(self, source, sink):
        path = self.find_path(source, sink, [])
        while path != None:
            residuals = [edge.capacity - self.flow[edge] for edge in path]
            flow = min(residuals)
            for edge in path:
                self.flow[edge] += flow
                self.flow[edge.redge] -= flow
            path = self.find_path(source, sink, [])
        return sum(self.flow[edge] for edge in self.get_edges(source))

g = FlowNetwork()
[g.add_vertex(v) for v in "sopqrt"]

print g.adj
print g.get_edges('s'), "@@@@"

g.add_edge('s','o',3)
g.add_edge('s','p',3)
g.add_edge('o','p',2)
g.add_edge('o','q',3)
g.add_edge('p','r',2)
g.add_edge('r','t',3)
g.add_edge('q','r',4)
g.add_edge('q','t',2)

print  "-"*100
print g.get_edges('s')
print "*"*100
print g.flow

print (g.max_flow('s','t'))
