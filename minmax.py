import math
import networkx as nx 
import matplotlib.pyplot as plt
from collections import deque

class Node:
  def __init__(self,name,value=None):
    self.name=name
    self.value=value
    self.children=[]
    self.minmax_value=None
  def add_child(self,child_node):
    self.children.append(child_node)
def minmax(node,is_maximizing_player):
  if not node.children:
    node.minmax_value=node.value
    return node.value    
  if is_maximizing_player:
    best_value=-math.inf
    for child in node.children:
      value=minmax(child,False)
      best_value=max(value,best_value)
    node.minmax_value=best_value
    return best_value
  else:
    best_value=math.inf
    for child in node.children:
      value=minmax(child,True)
      best_value=min(best_value,value)
    node.minmax_value=best_value
    return best_value
def build_tree():
  rootn=input("Enter the root value")
  root=Node(rootn) 
  queue=deque([root])
  while queue:
     cnode=queue.popleft()
     is_leaf=input(f"Whether {cnode.name} is leaf, y/n ").lower()
     if is_leaf=='y':
       value=int(input(f"Enter the value for {cnode.name} node"))
       cnode.value=value
     else:
       numchild=int(input(f"Enter no of chil for {cnode.name} node "))
       for i in range(numchild):
         child_name=input(f"Enter child {i+1} of {cnode.name}  ")
         child_name=Node(child_name)
         cnode.add_child(child_name)
         queue.append(child_name)
  return root
def build_graph(node,graph):
  if node is None:return
  for child in node.children:
    graph.add_edge(node.name,child.name)
    build_graph(child,graph)
def display(root):
  G=nx.DiGraph()
  build_graph(root,G)
  all_nodes=[]
  def get_all_nodes(node):
    if node:
      all_nodes.append(node)
      for child in node.children:
        get_all_nodes(child)
  get_all_nodes(root)
  labels={n.name:f"{n.name}\n[{n.minmax_value}]" for n in all_nodes}
  pos=nx.spring_layout(G)
  plt.figure(figsize=(10,7))
  nx.draw(G,pos,labels=labels,with_labels=True,arrows=False,node_size=2000,node_color='skyblue',font_size=12,font_weight='bold',width=2.0,edge_color='black')
  plt.title("Minmax Tree")
  plt.show()

if __name__=="__main__":      
   print("Minmax Algo")
   root=build_tree()
   if root:
     minmax(root,True)
     print(f"optimal value at root is {root.minmax_value}")
     display(root)
   else:
     print("No tree")

