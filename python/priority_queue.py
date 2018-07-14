#coding: UTF-8
# 优先队列

import heapq

pqueue = []

heapq.heappush(pqueue, (1, "A"))
heapq.heappush(pqueue, (7, "B"))
heapq.heappush(pqueue, (3, "C"))
heapq.heappush(pqueue, (6, "D"))
heapq.heappush(pqueue, (2, "E"))

print(pqueue)

heapq.heappop(pqueue)
heapq.heappop(pqueue)
heapq.heappop(pqueue)

heapq.heappush(pqueue, (5, "F"))

print(pqueue)
