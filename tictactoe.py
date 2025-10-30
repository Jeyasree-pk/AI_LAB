import math
HUMAN='O'
AI='X'
def display(board):
  print()
  for i in range(3):
    print(" | ".join(board[i*3:(i+1)*3]))
    if i<2:
     print("--+---+--")
  print(  )
def winner_move(board):
  win_states=[
    [0,1,2],[3,4,5],[6,7,8],
    [0,3,6],[1,4,7],[2,5,8],
    [0,4,8],[2,4,6]
  ]
  for state in win_states:
    if board[state[0]]==board[state[1]]==board[state[2]] and board[state[0]]!=' ':
      return board[state[0]]
  return None
def is_draw(board):
  return ' ' not in board and winner_move(board) is None
def minmax(board,is_maximizing):
  winner=winner_move(board)
  if winner==AI:
    return 1
  elif winner==HUMAN:
    return -1
  elif is_draw(board):
    return 0
  if is_maximizing:
    best_value=-math.inf
    for i in range(9):
      if board[i]==' ':
       board[i]=AI
       value=minmax(board,False)
       best_value=max(best_value,value)
       board[i]=' '
    return best_value
  else:
    best_value=math.inf
    for i in range(9):
      if board[i]==' ':
        board[i]=HUMAN
        value=minmax(board,True)
        best_value=min(best_value,value)
        board[i]=' '
    return best_value
def best_move(board):
  best_val=-math.inf
  move=None
  for i in range(9):
    if board[i]==' ':
      board[i]=AI
      score=minmax(board,False)
      board[i]=' '
      if score>best_val:
        best_val=score
        move=i
  return move
if __name__=="__main__":
 board=[' ']*9
 display(board)
 while True:
   move=int(input("Enter your move"))-1
   if 0<= move <9 and board[move]==' ':
     board[move]=HUMAN
     display(board)
   else:
      print("Invalid")  
   if winner_move(board):
     print("Hiuman wins")
     break
   if is_draw(board):
     print("it is a draw") 
     display(board)
     break
   move=best_move(board)
   board[move]=AI
   display(board)
   if winner_move(board):
     print("Ai wins")
     display(board)
     break
   if is_draw(board):
     print("It is a draw")
     display(board)

            
        
