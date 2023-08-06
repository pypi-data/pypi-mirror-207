def puzzle():
    print('8 puzzle imported...')
    s = """import copy  

from heapq import heappush, heappop   
n = 3  
  
rows = [ 1, 0, -1, 0 ]  
cols = [ 0, -1, 0, 1pyth ]  
 
class priorityQueue:  
 
    def __init__(self):  
        self.heap = []  

    def push(self, key):  
        heappush(self.heap, key)  

    def pop(self):  
        return heappop(self.heap)  
 
    def empty(self):  
        if not self.heap:  
            return True  
        else:  
            return False  
class nodes:  
      
    def __init__(self, parent, mats, empty_tile_posi,  
                costs, levels):  
 
        self.parent = parent  
        self.mats = mats  
        self.empty_tile_posi = empty_tile_posi  
        self.costs = costs  
        self.levels = levels  
    def __lt__(self, nxt):  
        return self.costs < nxt.costs  
def calculateCosts(mats, final) -> int:  
      
    count = 0  
    for i in range(n):  
        for j in range(n):  
            if ((mats[i][j]) and  
                (mats[i][j] != final[i][j])):  
                count += 1  
                  
    return count  
  
def newNodes(mats, empty_tile_posi, new_empty_tile_posi,  
            levels, parent, final) -> nodes:  
    new_mats = copy.deepcopy(mats)  
    x1 = empty_tile_posi[0]  
    y1 = empty_tile_posi[1]  
    x2 = new_empty_tile_posi[0]  
    y2 = new_empty_tile_posi[1]  
    new_mats[x1][y1], new_mats[x2][y2] = new_mats[x2][y2], new_mats[x1][y1]  
    costs = calculateCosts(new_mats, final)  
  
    new_nodes = nodes(parent, new_mats, new_empty_tile_posi,  
                    costs, levels)  
    return new_nodes  
def printMatsrix(mats):  
      
    for i in range(n):  
        for j in range(n):  
            print("%d " % (mats[i][j]), end = " ")  
              
        print()  
  
def isSafe(x, y):  
      
    return x >= 0 and x < n and y >= 0 and y < n  
def printPath(root):  
      
    if root == None:  
        return  
      
    printPath(root.parent)  
    printMatsrix(root.mats)  
    print()  
 
def solve(initial, empty_tile_posi, final):  
    pq = priorityQueue()  
    costs = calculateCosts(initial, final)  
    root = nodes(None, initial,  
                empty_tile_posi, costs, 0)  
    pq.push(root)  
    while not pq.empty():  
        minimum = pq.pop()  
        if minimum.costs == 0:  
            printPath(minimum)  
            return  
        for i in range(n):  
            new_tile_posi = [  
                minimum.empty_tile_posi[0] + rows[i],  
                minimum.empty_tile_posi[1] + cols[i], ]  
                  
            if isSafe(new_tile_posi[0], new_tile_posi[1]):  
                child = newNodes(minimum.mats,  
                                minimum.empty_tile_posi,  
                                new_tile_posi,  
                                minimum.levels + 1,  
                                minimum, final,)  
  
                pq.push(child)  

initial = [ [ 1, 2, 3 ],  
            [ 5, 6, 0 ],  
            [ 7, 8, 4 ] ]  
final = [ [ 1, 2, 3 ],  
        [ 5, 8, 6 ],  
        [ 0, 7, 4 ] ]  
  
empty_tile_posi = [ 1, 2 ]  
solve(initial, empty_tile_posi, final)"""
    return s

def vaccum():
    print("Agent Problem imported...")
    s = """import random

def display(room):
    print(room)

room = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
]
print("All the rooom are dirty")
display(room)

x =0
y= 0

while x < 4:
    while y < 4:
        room[x][y] = random.choice([0,1])
        y+=1
    x+=1
    y=0

print("Before cleaning the room I detect all of these random dirts")
display(room)
x =0
y= 0
z=0
while x < 4:
    while y < 4:
        if room[x][y] == 1:
            print("Vaccum in this location now,",x, y)
            room[x][y] = 0
            print("cleaned", x, y)
            z+=1
        y+=1
    x+=1
    y=0
pro= (100-((z/16)*100))
print("Room is clean now, Thanks")
display(room)
print('performance=',pro,'%')"""
    return s

def banana():
    s = """total=int(input('Enter no. of bananas at starting'))
distance=int(input('Enter distance you want to cover'))
load_capacity=int(input('Enter max load capacity of your camel'))
lose=0
start=total
for i in range(distance):
    while start>0:
        start=start-load_capacity
#Here if condition is checking that camel doesn't move back if there is only one banana left.
        if start==1:
            lose=lose-1#Lose is decreased because if camel try to get remaining one banana he will lose one extra banana for covering that two miles.
#Here we are increasing lose because for moving backward and forward by one mile two bananas will be lose
        lose=lose+2
#Here lose is decreased as in last trip camel will not go back.
    lose=lose-1
    start=total-lose
    if start==0:#Condition to check whether it is possible to take a single banana or not.
        break
print(start)
"""
    return s

def graphcolour():
    s = """G = [[ 0, 1, 1, 0, 1, 0],
	 [ 1, 0, 1, 1, 0, 1],
	 [ 1, 1, 0, 1, 1, 0],
	 [ 0, 1, 1, 0, 0, 1],
	 [ 1, 0, 1, 0, 0, 1],
	 [ 0, 1, 0, 1, 1, 0]]

# inisiate the name of node.
node = "abcdef"
t_={}
for i in range(len(G)):
	t_[node[i]] = i

# count degree of all node.
degree =[]
for i in range(len(G)):
	degree.append(sum(G[i]))

# inisiate the posible color
colorDict = {}
for i in range(len(G)):
	colorDict[node[i]]=["Blue","Red","Yellow","Green"]

# sort the node depends on the degree
sortedNode=[]
indeks = []

# use selection sort
for i in range(len(degree)):
	_max = 0
	j = 0
	for j in range(len(degree)):
		if j not in indeks:
			if degree[j] > _max:
				_max = degree[j]
				idx = j
	indeks.append(idx)
	sortedNode.append(node[idx])

# The main process
theSolution={}
for n in sortedNode:
	setTheColor = colorDict[n]
	theSolution[n] = setTheColor[0]
	adjacentNode = G[t_[n]]
	for j in range(len(adjacentNode)):
		if adjacentNode[j]==1 and (setTheColor[0] in colorDict[node[j]]):
			colorDict[node[j]].remove(setTheColor[0])

# Print the solution
for t,w in sorted(theSolution.items()):
	print("Node",t," = ",w)
"""
    return s

def money():
    s ="""def solutions():
    # letters = ('s', 'e', 'n', 'd', 'm', 'o', 'r', 'y')
    all_solutions = list()
    for s in range(9, -1, -1):
        for e in range(9, -1, -1):
            for n in range(9, -1, -1):
                for d in range(9, -1, -1):
                    for m in range(9, 0, -1):
                        for o in range(9, -1, -1):
                            for r in range(9, -1, -1):
                                for y in range(9, -1, -1):
                                    if len(set([s, e, n, d, m, o, r, y])) == 8:
                                        send = 1000 * s + 100 * e + 10 * n + d
                                        more = 1000 * m + 100 * o + 10 * r + e
                                        money = 10000 * m + 1000 * o + 100 * n + 10 * e + y

                                        if send + more == money:
                                            all_solutions.append((send, more, money))
    return all_solutions

print(solutions())
"""
    return s

def bfs():
    s = """graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited_bfs = []
queue = []

def bfs(visited_bfs, graph, node):
  visited_bfs.append(node)
  queue.append(node)

  while queue:
    s = queue.pop(0) 
    print (s, end = " ") 

    for neighbour in graph[s]:
      if neighbour not in visited_bfs:
        visited_bfs.append(neighbour)
        queue.append(neighbour)

visited = set()
print("BFS:" , end =" ")
bfs(visited_bfs, graph, 'A')
print('\n')
"""
    return s

def dfs():
    s = """graph = {
  'A' : ['B','C'],
  'B' : ['D', 'E'],
  'C' : ['F'],
  'D' : [],
  'E' : ['F'],
  'F' : []
}

visited_bfs = []
queue = []



visited = set()

def dfs(visited, graph, node):
    if node not in visited:
        print (node, end=" ")
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)


print('\n')
print("DFS:" , end =" ")
dfs(visited, graph, 'A')
"""
    return s

def water():
    s = """from collections import deque


def BFS(a, b, target):

	m = {}
	isSolvable = False
	path = []


	q = deque()

	q.append((0, 0))

	while (len(q) > 0):
		u = q.popleft()# If this state is already visited
		if ((u[0], u[1]) in m):
			continue
		if ((u[0] > a or u[1] > b or
			u[0] < 0 or u[1] < 0)):
			continue

		# Filling the vector for constructing
		# the solution path
		path.append([u[0], u[1]])

		# Marking current state as visited
		m[(u[0], u[1])] = 1

		# If we reach solution state, put ans=1
		if (u[0] == target or u[1] == target):
			isSolvable = True

			if (u[0] == target):
				if (u[1] != 0):

					# Fill final state
					path.append([u[0], 0])
			else:
				if (u[0] != 0):

					# Fill final state
					path.append([0, u[1]])

			# Print the solution path
			sz = len(path)
			for i in range(sz):
				print("(", path[i][0], ",",
					path[i][1], ")")
			break

		# If we have not reached final state
		# then, start developing intermediate
		# states to reach solution state
		q.append([u[0], b]) # Fill Jug2
		q.append([a, u[1]]) # Fill Jug1

		for ap in range(max(a, b) + 1):

			# Pour amount ap from Jug2 to Jug1
			c = u[0] + ap
			d = u[1] - ap

			# Check if this state is possible or not
			if (c == a or (d == 0 and d >= 0)):
				q.append([c, d])

			# Pour amount ap from Jug 1 to Jug2
			c = u[0] - ap
			d = u[1] + ap

			# Check if this state is possible or not
			if ((c == 0 and c >= 0) or d == b):
				q.append([c, d])

		# Empty Jug2
		q.append([a, 0])

		# Empty Jug1
		q.append([0, b])

	# No, solution exists if ans=0
	if (not isSolvable):
		print("No solution")


# Driver code
if __name__ == '__main__':

	Jug1, Jug2, target = 4, 3, 2
	print("Path from initial state "
		"to solution state ::")

	BFS(Jug1, Jug2, target)
"""
    return s

def best():
    s = """from queue import PriorityQueue
v = 14
graph = [[] for i in range(v)]

# Function For Implementing Best First Search
# Gives output path having lowest cost


def best_first_search(actual_Src, target, n):
	visited = [False] * n
	pq = PriorityQueue()
	pq.put((0, actual_Src))
	visited[actual_Src] = True
	
	while pq.empty() == False:
		u = pq.get()[1]
		# Displaying the path having lowest cost
		print(u, end=" ")
		if u == target:
			break

		for v, c in graph[u]:
			if visited[v] == False:
				visited[v] = True
				pq.put((c, v))
	print()

# Function for adding edges to graph


def addedge(x, y, cost):
	graph[x].append((y, cost))
	graph[y].append((x, cost))


# The nodes shown in above example(by alphabets) are
# implemented using integers addedge(x,y,cost);
addedge(0, 1, 3)
addedge(0, 2, 6)
addedge(0, 3, 5)
addedge(1, 4, 9)
addedge(1, 5, 8)
addedge(2, 6, 12)
addedge(2, 7, 14)
addedge(3, 8, 7)
addedge(8, 9, 5)
addedge(8, 10, 6)
addedge(9, 11, 1)
addedge(9, 12, 10)
addedge(9, 13, 2)

source = 0
target = 9
best_first_search(source, target, v)
"""
    return s

def astar():
    s = """import heapq

graph = {
    '5': {'3': 1, '7': 3},
    '3': {'2': 1, '4': 1},
    '7': {'8': 2},
    '2': {},
    '4': {'8': 1},
    '8': {}
}

def heuristic(n):
    H = {
        '5': 6,
        '3': 5,
        '7': 2,
        '2': 4,
        '4': 3,
        '8': 0
    }

    return H[n]

def a_star(graph, start, goal):
    frontier = [(0, start)]
    visited = set()
    parent = {start: None}
    g_score = {start: 0}

    while frontier:
        (f, current) = heapq.heappop(frontier)

        if current == goal:
            path = []
            while current is not None:
                path.append(current)
                current = parent[current]
            return list(reversed(path))

        visited.add(current)

        for neighbour in graph[current]:
            if neighbour not in visited:
                new_g_score = g_score[current] + graph[current][neighbour]

                if neighbour not in g_score or new_g_score < g_score[neighbour]:
                    g_score[neighbour] = new_g_score
                    f_score = new_g_score + heuristic(neighbour)
                    heapq.heappush(frontier, (f_score, neighbour))
                    parent[neighbour] = current

    return None

print(a_star(graph, '5', '8'))

"""
    return s

def unification():
    s = """def unification(a,b):
    if len(a) != len(b):
        return "Unification Failed"
    elif(a[0] != b[0]):
        return "Unification Failed"
    else:
        result = a[:2]
    
    for l in range(2,len(a)-1):
        result += a[l]
        if(a[l]==";"):
            continue
        result += "/"
        result += b[l]
    result += ")"

    print("Unification Success")
    return result
print("Enter Expression 1")
a = input()
print("Enter Expression 2")
b = input()
print(unification(a, b))
"""
    return s

def resolution():
    s = """from sympy import *

# Define the symbols and facts
A, B, C, D = symbols('A B C D')
facts = [A | B, B | C | D, ~C]

# Perform resolution
while True:
    new_facts = set()
    for i, fact1 in enumerate(facts):
        for j, fact2 in enumerate(facts):
            if i < j:
                for literal1 in fact1.args:
                    for literal2 in fact2.args:
                        if literal1 == ~literal2:
                            resolvent = Or(fact1.args.difference({literal1}), fact2.args.difference({literal2}))
                            if resolvent not in facts:
                                new_facts.add(resolvent)
        if ~fact1 in facts:
            print("Contradiction found")
            break
    else:
        if not new_facts:
            print("No new facts found")
            break
        facts = facts.union(new_facts)

# Print the final set of facts
print("Final set of facts:")
for fact in facts:
    print(fact)
"""
    return s

def nlp():
    s = """import re

# Define a list of example emails
emails = [
    'john.doe@example.com',
    'jane.doe@gmail.com',
    'smith@example.com',
    'mary123@hotmail.com',
    'peter_parker@web.com'
]

# Define a regular expression pattern for filtering emails
pattern = r'[a-zA-Z0-9._%+-]+@[gmail.]+\.[a-zA-Z]{2,}'

# Loop through each email and check if it matches the pattern
for email in emails:
    if re.match(pattern, email):
        print(email)

"""
    return s