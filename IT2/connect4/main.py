from turtle import width

import my_functions

WIDTH = 7
HEIGHT = 6


def check_vertical(x, y, player):

  counter = 0
  for n in range(4):
    try:
      if board[x][y + n] == str(player_piece[player]):
        counter += 1
        #print(counter)
    except:
      return False

    if counter == 4:
      return True

def check_horizontal(x, y, player):
  counter = 0
  for n in range(-4, 4):
    try:
      if board[x + n][y] == str(player_piece[player]):
        counter += 1
        print(counter)
    except:
      return False

    if counter == 4:
      return True
  

def check_diagonal_right():
  pass

def check_diagonal_left():
  pass


def swap_player(current_player):
  new_player = swap[current_player]
  return new_player

board = my_functions.create_board(WIDTH, HEIGHT)
my_functions.print_board(WIDTH, HEIGHT, board)

"""
Gameloop
----------------------------------------------------------
1. Ask the player for a number (1 - 7) V
2. Get the piece belonig to the player to the correct row V
3. Get the piece to the correct collumn V
4. Check for 4 in a row:
  Vertical V
  Horizontal V
  Diagonal right
  Diagonal left
5. Swap player V
6. Loop V
----------------------------------------------------------
"""

player_piece = {
  0: "X",
  1: "O"
}
swap = {0: 1, 1:0}
player = 0
move = None
legal_moves = [1, 2, 3, 4, 5, 6, 7]


while True:

  #  Asking the player for a number
  move = my_functions.ask_player(player, player_piece, legal_moves)
  if move == 0:
    break
  # Done asking the player
  placed_row = my_functions.place_piece(move, board, player_piece, player) 
  if placed_row == None:
    continue
  else:


    if check_vertical(move - 1, placed_row, player) or check_horizontal(move - 1, placed_row, player):
      print(f"Player {player_piece[player]} WON!")
      break

    my_functions.print_board(WIDTH, HEIGHT, board)

    player = swap_player(player)