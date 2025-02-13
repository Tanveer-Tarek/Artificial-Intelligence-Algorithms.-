def gbfs(graph, s, g, h):
	pq = [(h[s], s)]
	visited = set()
	while pq:
		pq.sort()  
		current_cost, current_node = pq.pop(0)
		if current_node == g:
			print(current_node,"	G is the Goal Node")
			return
		for neighbor, cost in graph[current_node]:  
			if neighbor not in visited:
				neighbor_cost = h[neighbor]
				pq.append((neighbor_cost, neighbor))
				visited.add(neighbor)

		print(current_node, "->",  end=" ")
	print("Goal not reached")




if __name__=="__main__":
	graph = {

		'A':[('B',1), ('C',3), ('D', 6)],
		'B':[('D',7), ('F',5)],
		'C':[('F',20)],
		'D':[('E',9)],
		'E':[('F',7)],
		'F':[('G',3)],
		'G':[]
		}
	starting_node = 'A'
	goal_node = 'G'
	heuristic = {
		'A':7,
		'B':2,
		'C':10,
		'D':15,
		'E':8,
		'F':6,
		'G':0
		}
	gbfs(graph, starting_node, goal_node, heuristic)




