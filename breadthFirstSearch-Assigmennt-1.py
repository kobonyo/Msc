import numpy as np
from collections import deque
def bfs(graph,nodes):
	nodeVisitState = {anode:False for anode in range(nodes)}
	queue = deque()# queue data structure
	queue.append(0) # add first node
	while len(queue): # while queue is not empty
		nodeToVisit = int(queue.pop()) # get node at the top
		print('Visiting '+str(nodeToVisit))
		if not nodeVisitState[nodeToVisit]:
			nodeVisitState[nodeToVisit] = True
			for anode in range(nodes):#loop all the nodes in graph
				if graph[nodeToVisit][anode] > 0 and not nodeVisitState[anode]:
					if anode not in queue: # avoid double entry 
						queue.appendleft(anode)

# testing the bfs with following adjacency matrix

adjacencyMatrix = [0, 1, 0, 1, 0, 0, 0, 0, 1],\
                  [1, 0, 0, 0, 0, 0, 0, 1, 0],\
                  [0, 0, 0, 1, 0, 1, 0, 1, 0],\
                  [1, 0, 1, 0, 1, 0, 0, 0, 0],\
                  [0, 0, 0, 1,0, 0, 0, 0, 1],\
                  [0, 0, 1, 0, 0, 0, 1, 0, 0],\
                  [0, 0, 0, 0, 0, 1, 0, 0, 0],\
                  [0, 1, 1, 0, 0, 0, 0, 0, 0],\
                  [1, 0, 0, 0, 1, 0, 0, 0, 0]

print(bfs(np.array(adjacencyMatrix),len(np.array(adjacencyMatrix))))
