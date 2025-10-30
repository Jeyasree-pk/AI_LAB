from collections import deque
def bfs(jg1,jg2,target):
  visited=set()
  queue=deque([((0,0),[])])
  
  while queue:
    (x,y), path =queue.popleft()
    if x==target or y==target:
      print(f" The target has been met {x},{y} ")
      print("->".join(str(pat) for pat in path))
      return True
    visited.add((x,y))
    next_state=set()
    next_state.add((jg1,y))
    next_state.add((x,jg2))
    next_state.add((0,y))
    next_state.add((x,0))
    transfer=min(x,jg2-y)
    next_state.add((x-transfer,y+transfer))
    transfer=min(y,jg1-x)
    next_state.add((x+transfer,y-transfer))
    for state in next_state:
      if state not in visited:
        queue.append((state,path+[(x,y)]))
        print("The next state",state)
  return 
def dfs(jg1,jg2,target):
  visited=set()
  stack=[((0,0),[(0,0)])]
  visited.add((0,0))
  while stack:
    (x,y),path=stack.pop()
    if x==target | y==target:
      print(f"Taeget found {x} {y} ")
      print(path)
      return True
    visited.add((x,y))
    next_state=set()
    next_state.add((jg1,y))
    next_state.add((x,jg2))
    next_state.add((0,y))
    next_state.add((x,0))
    transfer=min(x,jg2-y)
    next_state.add((x-transfer,y+transfer))
    transfer=min(y,jg1-x)
    next_state.add((x+transfer,y-transfer))
    for state in next_state:
      if state not in visited:
        visited.add(state)
        stack.append((state,path+[(x,y)]))
        print("The next state",state)
  return False    
        

if __name__=="__main__":
 jg1=int(input("Capacity of jg1"))
 jg2=int(input("Capacity for jg2"))
 target=int(input("Enter target"))
 bfs(jg1,jg2,target)
 dfs(jg1,jg2,target)
