import numpy as np
from collections import deque
def bfs(graph,nodes):
	nodeVisitState = {anode:False for anode in range(nodes)}
	queue = deque()
	queue.append(0)
	while len(queue):
		nodeToVisit = int(queue.pop())
		print('Visiting '+str(nodeToVisit))
		if not nodeVisitState[nodeToVisit]:
			nodeVisitState[nodeToVisit] = True
			for anode in range(nodes):#loop all the nodes in graph
				if graph[nodeToVisit][anode] > 0 and not nodeVisitState[anode]:
					if anode not in queue: # avoid double entry 
						queue.appendleft(anode)


adjaMat = [0, 1, 0, 1, 0, 0, 0, 0, 1],[1, 0, 0, 0, 0, 0, 0, 1, 0],[0, 0, 0, 1, 0, 1, 0, 1, 0],[1, 0, 1, 0, 1, 0, 0, 0, 0],\
          [0, 0, 0, 1,0, 0, 0, 0, 1],[0, 0, 1, 0, 0, 0, 1, 0, 0],[0, 0, 0, 0, 0, 1, 0, 0, 0],[0, 1, 1, 0, 0, 0, 0, 0, 0],\
          [1, 0, 0, 0, 1, 0, 0, 0, 0]
print(bfs(np.array(adjaMat),len(np.array(adjaMat))))
