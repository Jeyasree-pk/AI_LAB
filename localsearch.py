import random
import matplotlib.pyplot as plt
import networkx as nx
def conflicts(assignment,graph,colour,node):
  conflict=0
  for neighbour in graph[node]:
     if assignment.get(neighbour)==colour:
       conflict+=1
  return conflict
def min_conflict(graph,colours):
  steps=0
  assignment={node:random.choice(colours) for node in graph}
  while True:
    conflict_n=[]
    for node in graph:
      for neighbour in graph[node]:
        if assignment[node]==assignment[neighbour]:
          conflict_n.append(node)
          break
    if not conflict_n:
      print(f"Solution found in {steps} steps")
      return assignment
    node=random.choice(conflict_n)
    steps+=1  
    min_conf=float('inf')  
    best_colour=[]
    for colour in colours:
      conf=conflicts(assignment,graph,colour,node)
      if conf<min_conf:
        min_conf=conf
        best_colour=[colour]
      elif conf == min_conf:  
        best_colour.append(colour)
    assignment[node]=random.choice(best_colour)
  return assignment
def display(graph,assignment):
  G=nx.Graph()
  for node in graph:
    for neighbours in graph[node]:
      G.add_edge(node,neighbours)
  labels={n:n for n in graph }
  colour_map=[]
  for node in G.nodes():
    colour_map.append(assignment.get(node,'grey'))
  pos=nx.spring_layout(G,seed=42)
  plt.figure(figsize=(10,8))
  nx.draw(G,pos,labels=labels,with_labels=True,node_color=colour_map,node_size=2000,font_size=12,font_weight='bold',edge_color='black')
  plt.title("Graph colour")
  plt.show()

if __name__=="__main__":
  node=[]
  graph={}
  colours=[]
  n=int(input("Enter no of node"))
  for i in range(n):
   ed=input(f"Enter node {i+1} ")
   node.append(ed)
  ne=int(input("Enter no of edges"))
  for i in range(ne):
    node1,node2=input(f"Enter edge {i+1} ").split()
    if node1 not in graph:
      graph[node1]=[]
    if node2 not in graph:
      graph[node2]=[]
    graph[node1].append(node2)
    graph[node2].append(node1)
  nc=int(input("Enter no of colours"))
  for i in range(nc):
    c=input(f"Enter color {i+1} ")
    colours.append(c)
  assignment=min_conflict(graph,colours)  
  print("Assignment",assignment)
  display(graph,assignment)
    
