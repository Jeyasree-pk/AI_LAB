def tsp(start_node,graph):
  all_nodes=set(graph.keys())
  for nodes in graph:
    all_nodes.update(graph[nodes].keys())
  tour=[start_node]
  visited=set(start_node)
  total_cost=0
  cnode=start_node
  while len(tour)<len(all_nodes):
    neigh=None
    min_cost=float('inf')
    for node,cost in graph.get(cnode,{}).items():
     if node not in visited and cost<min_cost:
       min_cost=cost
       neigh=node
    if node:
      tour.append(neigh) 
      visited.add(neigh)
      total_cost+=min_cost
      cnode=neigh
  last_node=tour[-1]
  if start_node in graph.get(last_node,{}):
    scost=graph[last_node][start_node]
    total_cost+=scost
    tour.append(start_node)
  return tour,total_cost
if __name__=="__main__":
  graph={}
  ne=int(input("Enter no of edges"))
  for i in range(ne):
    node1,node2,cost=input(f"Enter {i+1} edge with cost").strip().split()
    cost=int(cost)
    if node1 not in graph:
      graph[node1]={}
    if node2 not in graph:
      graph[node2]={}
    graph[node1][node2]=cost 
    graph[node2][node1]=cost
  start=input("Enter start ")
  tour,total_cost=tsp(start,graph)
  if tour:
    print(tour)
    #print(f"tour" ,"->".join(tour))
    print(f"Tptal cost {total_cost}")
    

