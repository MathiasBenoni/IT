from turtle import width

import check_win
import bot_0
import bot_1
import bot_2
import bot_3

swap = {0: 1, 1:0}

def create_board(width, height):
  board = []
  for x in range(width):
    column = []

    for y in range(height):
      column.append(" ")

    board.append(column)
  return board

def print_board(width, height, board, player_piece, colors, backgrounds):
  piece_to_player = {piece: p for p, piece in player_piece.items()}

  print()

  for y in range(height):
    print("|", end="")
    for x in range(width):
      cell = board[x][y]
      if cell == " ":
        print(cell + "|", end="")
      else:
        owner = piece_to_player[cell]
        print(colors[owner] + backgrounds[owner] + cell + colors["White"] + backgrounds["No"] + "|", end="")
    print()

  print("---------------")
  print("|1|2|3|4|5|6|7|")
  print()

def ask_player(player, player_piece, legal_moves):
  while True:
    try:
      move = int(input(f"Player {player_piece[player]} (1 - 7): "))
      if move == 0:
        print("Bye!")
        return move
      if move in legal_moves:
        return move
      else:
        print("Try again")
    except ValueError:
      print("Try again")

def place_piece(move, board, player_piece, player):
  x = move - 1
  column = board[x]

  for y in range(len(column) - 1, -1, -1):
    if column[y] == " ":
      column[y] = str(player_piece[player])
      return y

  print("Column full")
  return None

def swap_player(current_player):
  new_player = swap[current_player]
  return new_player

def play_turn(move, player, player_piece, board, width, height, colors, backgrounds):
  placed_row = place_piece(move, board, player_piece, player)
  if placed_row is None:
    return player  # column full, same player retries

  print_board(width, height, board, player_piece, colors, backgrounds)

  if check_win.check_win(move - 1, placed_row, player_piece, player, board):
    print(f"Player {player_piece[player]} WON!")
    return None

  return swap_player(player)

def get_bot_move(model, board, player, player_piece, depth=4):
  match model:
    case 0:
      print(len(board[0]))
      return bot_0.make_move(len(board[0]) + 1)
    case 1:
      return bot_1.make_move(board, player, player_piece)
    case 2:
      return bot_2.make_move(board, player, player_piece)
    case 3:
      return bot_3.make_move(board, player, player_piece, depth)
