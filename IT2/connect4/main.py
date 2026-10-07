import my_functions
import check_win

WIDTH = 7
HEIGHT = 6


colors = {
  0: "\x1b[31m",
  1: "\x1b[34m",
  "White": "\x1b[37m",
}
backgrounds = {
  0: "\x1b[41m",
  1: "\x1b[44m",
  "No": "\x1b[49m"
}

player_piece = {
  0: "X",
  1: "O"
}

player = 0
move = None
legal_moves = [1, 2, 3, 4, 5, 6, 7]

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



while True:

  #  Asking the player for a number
  move = my_functions.ask_player(player, player_piece, legal_moves)
  if move == 0:
    break
  # Done asking the player
  placed_row = my_functions.place_piece(move, board, player_piece, player, colors, backgrounds) 
  if placed_row == None:
    continue
  else:

    my_functions.print_board(WIDTH, HEIGHT, board)

    if check_win.check_win(move - 1, placed_row, player_piece, player, board):
      print(f"Player {player_piece[player]} WON!")
      break

    player = my_functions.swap_player(player)