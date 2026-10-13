import random

import my_functions
import check_win

swap = {0: 1, 1:0}

player_piece = {
  0: "X",
  1: "O"
}

def swap_player(current_player):
  new_player = swap[current_player]
  return new_player

def place_piece(move, board, player_piece, player):
  x = move - 1
  column = board[x]

  for y in range(len(column) - 1, -1, -1):
    if column[y] == " ":
      column[y] = player_piece[player]
      return y

  print("Column full")
  return None

def make_move(main_board, x, y, player, player_piece):
  local_board = main_board

  local_move = random.randint(1, 7)
  for x in range(7):
    if check_win.check_win(x, y, player_piece, player, local_board):
      print("WIN")
    elif check_win.check_win(x, y, player_piece, swap_player(player)):
      print("LOSS")
    else:
      move = random.randint(1, 7)



board = my_functions.create_board(7, 6)
move = random.randint(1, 7)

y = place_piece(move, board, player_piece, 0)

make_move(board, move, y, 0, player_piece)

print(move, y)