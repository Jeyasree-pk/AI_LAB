import math
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
  def __init__(self,name,value=None):
    self.name=name
    self.value=value
    self.minmax_value=None
    self.is_pruned=False
    self.children=[]
  def add_child(self,child_node):
    self.children.append(child_node)
    
def build_tree():
  root=input("Enter root node ")
  root=Node(root)
  queue=deque([root])
  while queue:
    cnode=queue.popleft()
    is_leaf=input(f"Enter whether {cnode.name} is leaf node, y/n").lower()
    if is_leaf=='y':
      value=int(input(f"Enter the value of {cnode.name} "))
      cnode.value=value
    else:
      child_num=int(input(f"Enter no of child for {cnode.name} "))
      for i in range(child_num):
        child_name=input(f"Enter child {i+1} of {cnode.name} ")
        child_name=Node(child_name)
        cnode.add_child(child_name)
        queue.append(child_name)
  return root
def alpha_beta(node,is_maximizing,alpha,beta):
  if not node.children:
    node.minmax_value=node.value
    return node.value
  if is_maximizing:
    best_value=-math.inf
    for i,child in enumerate(node.children):
     value=alpha_beta(child,False,alpha,beta)
     best_value=max(value,best_value)
     alpha=max(alpha,best_value)
     if beta<=alpha:
       for remaining_n in node.children[i+1:]:
        remaining_n.is_pruned=True
       break  
    node.minmax_value=best_value   
  else:
    best_value=math.inf
    for i,child in enumerate(node.children):
     value=alpha_beta(child,True,alpha,beta)
     best_value=min(best_value,value)
     beta=min(best_value,beta)
     if beta<=alpha:
       for remaining_n in node.children[i+1:]:
         remaining_n.is_pruned=True
       break 
    node.minmax_value=best_value
  return best_value  

def build_graph(node,graph):
  if node is None:return
  else:
    for child in node.children:
      graph.add_edge(node.name,child.name)
      build_graph(child,graph)
def display(node):
  G=nx.DiGraph() 
  build_graph(node,G)
  all_node=[]
  def node_list(node):
   if node: 
    all_node.append(node)
    for child in node.children:
      node_list(child) 
  node_list(node)
  node_n={n.name: n for n in all_node} 
  label_n={n.name:f"{n.name}\n{[n.minmax_value]}" for n in all_node}
  
  edge_colour=['grey' if node_n.get(v).is_pruned else 'skyblue' for u,v in G.edges]
  edge_style=['dashed' if node_n.get(v).is_pruned else 'solid' for u,v in G.edges]
  node_colours=['grey' if node_n.get(n).is_pruned else 'skyblue' for n in G.nodes]
  pos=nx.spring_layout(G)
  plt.figure(figsize=(10,7))
  plt.title("Alpha beta pruning")
  
  nx.draw(G,pos,labels=label_n,with_labels=True,arrows=False,node_size=2000,node_color=node_colours,width=2,font_size=12,font_weight='bold',edge_color=edge_colour,style=edge_style) 
  plt.show()

if __name__=="__main__":
  root=build_tree()
  if root:
    print("alpha beta")
    best=alpha_beta(root,True,-math.inf,math.inf)
    print(f"optimal {best}")
    display(root) 
