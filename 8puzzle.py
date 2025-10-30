import heapq
def printpuzzle(state):
  for i in range(0,9,3):
    print(" ".join(map(str,state[i:i+3])).replace('0','_'))
  print()
def misplaced(initial,goal):
  misplaced=0
  for i in range(9):
    if initial[i]!=goal[i] and initial[i]!=0:
      misplaced+= 1
  return misplaced
def manhattan(initial,goal):
  dist=0
  for i in range(9):
    if initial[i]!=0:
      row,col=divmod(i,3)
      goalrow,goalcol=divmod(goal.index(initial[i]),3)
      dist+=abs(row-goalrow)+abs(col-goalcol)
  return dist
def successors(initial):
  successor=[]
  blankind=initial.index(0)
  row,col=divmod(blankind,3)
  moves=[(-1,0),(0,-1),(1,0),(0,1)]
  for dx,dr in moves:
    newr,newcol=dx+row,dr+col
    if(0<=newr<3 and 0<=newcol<3):
      index=newr*3+newcol
      newstate=list(initial)
      newstate[blankind],newstate[index]=newstate[index],newstate[blankind]
      successor.append(tuple(newstate))
  return successor  
def astar(initial,goal,heuristic):
  queue=[(0,0,initial,[initial])]
  explored_state=set()
  while queue:
    f,g,cstate,path=heapq.heappop(queue)
    if cstate in explored_state:
      continue
    explored_state.add(cstate)
    if goal==cstate:
      return path,len(explored_state)
    for successor in successors(cstate):
      if successor not in explored_state:
        newg=g+1
        hcost=heuristic(successor,goal)
        newf=hcost+newg
        heapq.heappush(queue,(newf,newg,successor,path+[successor]))
  return None,len(explored_state)
if __name__=="__main__":
  try: 
   initial_input=input("Enter initial state: ").strip().split()
   initial_input=tuple(map(int,initial_input))
   if len(initial_input)!=9 or len(set(initial_input))!=9:
      raise ValueError
  except ValueError:
     print("Invalid input.")
     exit()
  goal_input=input("Enter goal state: ").strip().split()
  goal_input=tuple(map(int,goal_input))
  choice=int(input("Enter 1 for misplaced and 2 for manhattan "))
  while True:
   if choice==1:
    heuristic=misplaced
   elif choice==2:
    heuristic=manhattan
   else: 
    print("Invalid choice")
    exit()
   
   print("Solving")
   path,visited=astar(initial_input,goal_input,heuristic)
   if path:
    print("Solution found")
    print(f"totsl moves {len(path)-1} ")
    for i,state in enumerate(path):
      print(f"state {i} ")
      printpuzzle(state)
   else:
    print("No solution found")
   choice=int(input("Enter 1 for misplaced and 2 for manhattan "))

