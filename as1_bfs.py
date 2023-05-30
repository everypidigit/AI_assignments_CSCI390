#Author: Dinh-Mao Bui, Anh-Tu Nguyen
#Rule of traversing: Alphabetical ordered, then left to right, 

#Points: 2
def traverse(tree, init):    	#DONE
	queue = [init]
	traversed = []
	while queue:
		node = queue.pop(0)
		# if a node has already been visited, then do not push it to the traversed ones, just mark it.
		# push to the list only if it is a new node
		if node in traversed: pass	
		else: traversed.append(node)	
		leaves = tree[node]
  		# same thing applies to the leaves. do not append if it is not a new leaf
		for leaf in leaves:
			if leaf in traversed:  
				pass
			else: 
				queue.append(leaf)
	return traversed

#Points: 3
def pathfinder(tree, init, goal):
	traversed = []
	queue = [init] # the queue is now the initial state that we have provided to the function
	if init == goal:
		return "No kidding, pls"
	while queue:
		node = queue.pop(0)	
		if node in traversed: pass
		else: traversed.append(node)
  
		leaves = tree[node]
		for leaf in leaves:  
			# check if the current leaf is our goal. if it is, append it to the traversed and just return the list
			if leaf == goal:
				traversed.append(leaf)
				return traversed
			else: 
				if leaf in traversed: 
					pass
				else: 
					queue.append(leaf)
	return "No such path exists"
	
 
