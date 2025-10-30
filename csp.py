def is_valid(color,region,neighbours,assignment):
  for neighbour in neighbours.get(region,[]):
    if neighbour in assignment and assignment[neighbour]==color:
      return False
  return True
def backtracking(colors,regions,neighbours,assignment):
  if len(assignment)==len(regions):
     return assignment
  for region in regions:
    if region not in assignment:
      break
  for color in colors:
    if is_valid(color,region,neighbours,assignment):
      assignment[region]=color
      result=backtracking(colors,regions,neighbours,assignment)
      if result:
        return result
      del assignment[region]
  return None

if __name__ == "__main__" :
  nr=int(input("Enter n region "))
  regions=[]
  neighbours={}
  for i in range(nr):
   r=input(f"Enter {i+1} region ")
   regions.append(r)
  m=int(input("Enter n color "))
  colors=[]
  for i in range(m):
    c=input(f"enter {i+1} color ")
    colors.append(c)
  n=int(input("Enter no of edges "))
  print("Enter all edges as a pair")
  assignment={}
  for i in range(n):
    node1,node2=input(f"Edge {i+1} ").strip().split()
    if node1 not in neighbours:
     neighbours[node1] = []
    if node2 not in neighbours:
     neighbours[node2] = []
    neighbours[node1].append(node2)
    neighbours[node2].append(node1)
print("Neighbours:", neighbours)


print("regions",regions)  
result=backtracking(colors,regions,neighbours,assignment)
if result:
   for region,color in result.items():
    print(f"{region}->{color}")
print(assignment)
import networkx as nx
import matplotlib.pyplot as plt

G=nx.Graph()
for node,adj in neighbours.items():
  for neighbhour in adj:
    G.add_edge(node,neighbhour)
node_colors=[assignment.get(node,"grey") for node in G.nodes()]
plt.figure(figsize=(8,8))
pos=nx.spring_layout(G,seed=42)
nx.draw(G,pos,with_labels=True,node_color=node_colors,node_size=2000,font_size=12,font_color='white',width=2.0,edge_color='grey')
plt.title("Map coloring Using CSV")
plt.show()
