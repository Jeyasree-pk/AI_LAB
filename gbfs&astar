import heapq
def gbfs(heuristic,start,goal,graph):
  visited=set()
  path=[]
  queue=([(heuristic[start],start,[start])])
  visited.add(start)
  while queue:
   h,node,path=heapq.heappop(queue) 
   print(node,end=" ")
   if goal==node:
     print("Goal is found")
     print(path)
     return path
   for no in graph[node]:
     if no not in visited:
       visited.add(no)
       heapq.heappush(queue,(heuristic[no],no,path+[no]))
  return
def astar(heuristic,graph,start,goal):
  queue=([(heuristic[start],0,start,[start])])
  ming={start:0}
  while queue:
    h,g,node,path=heapq.heappop(queue)
    if g>ming.get(node,float("inf")):
      continue
    if node==goal:
      print("Goal found ")
      return path,g
    for no,cost in graph[node].items():
      newg=g+cost
      if newg<ming.get(no,float('inf')):
        ming[no]=newg
        newf=newg+heuristic[no]
        heapq.heappush(queue,(newf,newg,no,path+[no]))
  return


if __name__=="__main__":
  graph={}
  nod=[]
  heuristic={}
  n=int(input("Enter no of nodes "))
  for i in range(n):
    nodes,hval=input(f"Enter node {i+1} with heuristic ").split()
    heuristic[nodes]=int(hval)
    nod.append(nodes)
  ne=int(input("Enter no of edges "))
  print("Enter the edges and cost")
  for i in range(ne):
    node1,node2,cost=input(f"edge {i+1} ").split()
    cost=int(cost)
    if node1 not in graph:
     graph[node1] = {}
    if node2 not in graph:
     graph[node2] = {}
    graph[node1][node2]=cost
    graph[node2][node1]=cost
  start=input("Enter start node")
  goal=input("Enter goal node")
  path=gbfs(heuristic,start,goal,graph)
  path,g=astar(heuristic,graph,start,goal)
  totalcost=0
  for i in range(len(path)-1):
     edgecost=graph[path[i]][path[i+1]]
     totalcost+=edgecost
  print(f"Total cost {totalcost} ")
