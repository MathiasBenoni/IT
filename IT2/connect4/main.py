import my_functions
import check_win
import bot_0
import bot_1

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
4. Check for 4 in a row: V
  Vertical V
  Horizontal V
  Diagonal right V
  Diagonal left V
5. Swap player V
6. Loop V
----------------------------------------------------------
"""

nisse = input("Want to play against Da Bot? (Y / N): ")

if nisse.lower() == "n":
  bot = False
else:
  bot = True
  model = int(input("How strong should Da Bot be? (0 - 1): "))

def get_bot_move(model, width):
  match model:
    case 0:
      return bot_0.make_move(width)
    case 1:
      return None

while True:
  move = my_functions.ask_player(player, player_piece, legal_moves)
  if move == 0:
    break

  player = my_functions.play_turn(move, player, player_piece, board, WIDTH, HEIGHT, colors, backgrounds)
  if player is None:
    break

  match model:
    case 0:
      move = get_bot_move(model, WIDTH)

      if move is not None:
            print(f"Da Bot chose column {move}")
            player = my_functions.play_turn(move, player, player_piece, board, WIDTH, HEIGHT, colors, backgrounds)
            if player is None:
              break
