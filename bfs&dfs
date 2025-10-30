from collections import deque
def bfs(start,goal,graph):
  visited=set()
  queue=deque([(start,[start])])
  visited.add(start)
  path=[]
  while queue:
    cur,path=queue.popleft()
    print(cur,end =" ")
    if cur==goal:
      print("Goal is found")
      print("path","->".join(path))
    for node in graph[cur]:
       if node not in visited:
         visited.add(node)
         queue.append((node,path+[node]))
  return
def dfs(start,goal,graph,visited=None):
  if visited is None:
    visited=set()
  visited.add(start)
  print(start,end="")
  if start==goal:
      print("Goal is found")
  for node in graph[start]:
      if node not in visited:
        visited.add(node)
        if dfs(node,goal,graph,visited):
         return True
  return False        
    
if __name__== "__main__" :
   graph={}
   node=[]
   n=int(input("Enter no of nodes "))
   for i in range(n):
     no=input(f"Enter node {i+1} ")
     node.append(no)
   ne=int(input("Enter np of edges"))
   print("Enter edges as pair")
   for i in range(ne):
     node1,node2=input(f"Enter edge {i+1} ").split()
     if node1 not in graph:
       graph[node1]=[]
     if node2 not in graph:
       graph[node2]=[]
     graph[node1].append(node2)
     graph[node2].append(node1)
   print(node)
   print(graph)
   start=input("Enter start")
   goal=input("Enter goal")  
   while i!=3:
  
    dfs(start,goal,graph,visited=None)

