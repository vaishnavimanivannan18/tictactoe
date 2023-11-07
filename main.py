user_moves = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']

def show_board(user_moves):
  # printing the board with the user moves
  print(f" {user_moves[1]} | {user_moves[2]} | {user_moves[3]}")
  print(f"---|---|---")
  print(f" {user_moves[4]} | {user_moves[5]} | {user_moves[6]}")
  print(f"---|---|---")
  print(f" {user_moves[7]} | {user_moves[8]} | {user_moves[9]}")

show_board([' ','1','2','3','4','5','6','7','8','9',])


def check_winner(board):
  if board[1]==board[4] and board[4]==board[7] and board[1]!=' ':
   print ("a player has won") 
  else:
    print("continue playing or if positions are taken then it is a draw")
  if board[2]==board[5] and board[5]==board[8] and board[2]!=' ':
    print ("a player has won") 
  if board[3]==board[6] and board[6]==board[9] and board[3]!=' ':
    print ("a player has won") 
  if board[1]==board[2] and board[2]==board[3] and board[1]!=' ':
    print ("a player has won") 
  if board[4]==board[5] and board[5]==board[6] and board[4]!=' ':
    print ("a player has won") 
  if board[7]==board[8] and board[8]==board[9] and board[7]!=' ':
    print ("a player has won") 
  if board[1]==board[5] and board[5]==board[9] and board[1]!=' ':
    print ("a player has won") 
  if board[3]==board[5] and board[5]==board[7] and board[3]!=' ':
    print ("a player has won")

#CHECKING IF THE INPUT IS ALREADY DONE (IF USER INPUT IS VALID)
bool = False

#SETTING PLAYERS X
the_player='X'

while not False:
  try:
    the_move = int(input(f"Player {the_player} enter your move: "))
    if (the_move < 1 or the_move > 9):
      print("invalid, enter a number between 1 and 9")
    else:
      playing = True
      if user_moves[the_move]!=' ':
       print("this is already taken, pick another number")
      else:

      
        if the_player =='O':
          user_moves[the_move] = 'O'
        else:
          user_moves[the_move] ='X'
      
      show_board(user_moves)
      if the_player == 'X':
        the_player = 'O'
      else:
       the_player = 'X'
      check_winner(user_moves)
  except:
    print("Incorrect data entered. Try again!")
    bool = True


  # Run the game  
if user_moves[the_move]!=' ':
 print("error message square is already taken pick another one")
else:
  user_moves[the_move] ='X'


